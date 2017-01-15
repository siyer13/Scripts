import logging
import os.path
import psycopg2
import sys
import re
from datetime import datetime, timedelta, date
from urlparse import urlparse
from time import sleep
from sh import tail
from sh import awk
import subprocess
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks import ConfigurationHook
from airflow.hooks import UtilHook as utils
from slackclient import SlackClient
from airflow import configuration

class HiveJobMonitor:
    """
    HiveJobMonitor is for monitoring the hivejob that are in running state in
    the airflow database. In any case the job hangs in hadoop cluster but is still
    in running state, the monitor clears the jobs and the backfill command picks
    it up.
    """
    home_dir = os.path.expanduser('~')

    def __init__(self, args, dag_name):
        self.dag_name = dag_name
        self.args = args

    def xstr(self, password):
        if password is None:
            return ''
        else:
            return str(password)

    def send_notification(self, channel_id, message):
        slack_client = SlackClient(self.args['slack_api_token'])
        slack_client.api_call('chat.postMessage', channel=channel_id, text=message, username=self.args['slack_bot'], icon_emoji=self.args['slack_avatar_icon_url'])

    def clear_n_rerun(self, command, task_id, dag_id):
        clear_n_rerun = 'sh ' + self.home_dir + '/scripts/clear_n_rerun.sh ' + command + ' '  + task_id + ' ' + dag_id
        subprocess.call(clear_n_rerun.split(), shell=False)
        logging.info(task_id + ' cleared.')
        if command == 'backfill':
            self.send_notification(self.args['slack_channel'], 'Pipeline stuck, backfill triggered.')
        else:
            self.send_notification(self.args['slack_channel'], task_id + ' cleared and re-ran.')

    def job_monitor(self):
        current_date = date.today()
        log_folder = os.path.expanduser(configuration.get('core', 'BASE_LOG_FOLDER'))
        sql_alchemy_conn = os.path.expanduser(configuration.get('core', 'SQL_ALCHEMY_CONN'))
        conn = urlparse(sql_alchemy_conn)
        log_file = log_folder + '/' + self.dag_name + '/'
        DAG_ID = self.dag_name
        db_name = conn.path[1:]
        user_name = conn.username
        host_name = conn.hostname
        pswd = self.xstr(conn.password)
        try:
            db_conn = psycopg2.connect('dbname=' + db_name + ' user=' + user_name + ' host=' + host_name + ' password=' + pswd)
            logging.info('Database connection acquired')
        except:
            logging.error('Unable to connect to the database')

        cur = db_conn.cursor()
        while True:
            cur.execute('SELECT state FROM  task_instance WHERE execution_date = %(EXECUTION_DATE)s AND dag_id = %(DAG_ID)s AND task_id = %(TASK_ID)s ORDER BY execution_date DESC', {'EXECUTION_DATE': current_date.isoformat() + ' 00:00:00','DAG_ID': DAG_ID,'TASK_ID': 'done'})
            state = cur.fetchone()[0]
            if state == 'success':
                break
            else:
                cur.execute('SELECT task_id, state FROM  task_instance WHERE execution_date = %(EXECUTION_DATE)s AND dag_id = %(DAG_ID)s AND (state = %(RUNNING_STATE)s OR state = %(SHUTDOWN_STATE)s ) order by execution_date desc', {'EXECUTION_DATE': current_date.isoformat() + ' 00:00:00','DAG_ID': DAG_ID,'RUNNING_STATE': 'running','SHUTDOWN_STATE': 'shutdown'})
                task_ids = cur.fetchall()
                for task_id in task_ids:
                    log_line = str(tail('-1', log_file + str(task_id[0]) + '/' + str(str(current_date) + 'T00:00:00')))
                    output = awk(awk(tail('-50', log_file + '/log_monitor/' + str(str(current_date) + 'T00:00:00')), "-F", " ", "{print $9}"),"-F","/","{print $7}")
                    tasks = set()
                    for task in output:
                        tasks.add(task)
                    tasks.remove('\n')
                    if len(tasks) == 1:
                            self.clear_n_rerun_job('backfill', task_id[0], DAG_ID)
                    date_string = re.search('\\d{4}-\\d{2}-\\d{2}\\s\\d{2}:\\d{2}:\\d{2}', log_line)
                    date_string = date_string.group(0)
                    last_timestamp = datetime.strptime(str(date_string), '%Y-%m-%d %H:%M:%S')
                    current_timestamp = datetime.now()
                    time_diff = (current_timestamp - last_timestamp).total_seconds() / 60
                    if time_diff >= 7:
                        self.send_notification(self.args['slack_channel'], task_id[0] + ' stuck in PvA pipeline')
                        self.clear_n_rerun('clear_n-rerun',task_id[0], DAG_ID)
                    else:
                        sleep(100)
