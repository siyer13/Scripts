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




class JobMonitor:
    """
    JobMonitor is for monitoring the jobs that are in running state in
    the airflow database. In any case the job hangs in hadoop cluster but is still
    in running state, the monitor clears and runs the job again.
    """
    home_dir = os.path.expanduser('~')

    def __init__(self):
        pass

    def initialize_logger(self,output_dir):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        current_date = date.today().isoformat()
        log_file = str(current_date) + '.log'

        # create console handler and set level to info
        # handler = logging.StreamHandler()
        # handler.setLevel(logging.INFO)
        # formatter = logging.Formatter("[%(asctime)s] {%(filename)s} %(levelname)s - %(message)s")
        # handler.setFormatter(formatter)
        # logger.addHandler(handler)

        # create error file handler and set level to error
        handler = logging.FileHandler(os.path.join(output_dir, log_file),"a", encoding=None, delay="true")
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter("[%(asctime)s] {%(filename)s} %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        #create INFO file handler and set level to INFO
        handler = logging.FileHandler(os.path.join(output_dir, log_file),"a")
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter("[%(asctime)s] {%(filename)s} %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)


    def xstr(self, password):
        return str(password or '')

    def send_notification(self, channel_id, message):
        slack_client = SlackClient('xoxb-14353465654534-4pYzTpFk55nLreifdsa3fas22F')
        logging.info('slack')
        slack_client.api_call('chat.postMessage', channel=channel_id, text=message)

    def restart(self, command, dag_id, task_id=''):
        clear_n_rerun = 'sh ' + self.home_dir + '/scripts/clear_n_rerun.sh ' + command + ' '  + dag_id +  ' ' + task_id
        self.send_notification('siyer_airflow', 'PvA pipeline seems to be stuck, clearing and re-running')
        logging.info(clear_n_rerun)
        subprocess.call(clear_n_rerun.split(), shell=False)

    def job_monitor(self,dag_name,log_dir):
        self.initialize_logger(log_dir)
        current_date = date.today()
        log_folder = os.path.expanduser(configuration.get('core', 'BASE_LOG_FOLDER'))
        sql_alchemy_conn = os.path.expanduser(configuration.get('core', 'SQL_ALCHEMY_CONN'))
        conn = urlparse(sql_alchemy_conn)
        log_file = log_folder + '/' +dag_name + '/'
        monitor_log = log_dir + str(current_date) + '.log'
        DAG_ID = dag_name
        db_name = conn.path[1:]
        user_name = conn.username
        host_name = conn.hostname
        pswd = self.xstr(conn.password)
        print 'dbname=' + db_name + ' user=' + user_name + ' host=' + host_name + ' password=' + pswd
        try:
            db_conn = psycopg2.connect('dbname=' + db_name + ' user=' + user_name + ' host=' + host_name + ' password=' + pswd)
            logging.info('Database connection acquired')
        except:
            logging.info('Unable to connect to the database')

        cur = db_conn.cursor()
        cur.execute('SELECT state FROM  task_instance WHERE execution_date = %(EXECUTION_DATE)s AND dag_id = %(DAG_ID)s AND task_id = %(TASK_ID)s ORDER BY execution_date DESC', {'EXECUTION_DATE': current_date.isoformat() + ' 00:00:00','DAG_ID': DAG_ID,'TASK_ID': 'done'})
        if cur.rowcount == 0:
            logging.info(str(DAG_ID) + ' execution not started')
        else:
            state = cur.fetchone()[0]
            if state == 'success':
                logging.info(str(DAG_ID) + ' execution completed for the day')
            else:
                cur.execute('SELECT task_id, state FROM  task_instance WHERE execution_date = %(EXECUTION_DATE)s AND dag_id = %(DAG_ID)s AND (state = %(RUNNING_STATE)s OR state = %(SHUTDOWN_STATE)s ) order by execution_date desc', {'EXECUTION_DATE': current_date.isoformat() + ' 00:00:00','DAG_ID': DAG_ID,'RUNNING_STATE': 'running','SHUTDOWN_STATE': 'shutdown'})
                task_ids = cur.fetchall()
                logging.info('Running tasks: ' + str(task_ids))
                for task_id in task_ids:
                    log_line = str(tail('-1', log_file + str(task_id[0]) + '/' + str(str(current_date) + 'T00:00:00')))
                    logging.info(log_line)
                    date_string = re.search('\\d{4}-\\d{2}-\\d{2}\\s\\d{2}:\\d{2}:\\d{2}', log_line)
                    date_string = date_string.group(0)
                    last_timestamp = datetime.strptime(str(date_string), '%Y-%m-%d %H:%M:%S')
                    current_timestamp = datetime.now()
                    time_diff = (current_timestamp - last_timestamp).total_seconds() / 60
                    logging.info('time diff: ' + str(time_diff))
                    if time_diff >= 15:
                        #self.send_notification(self.args['slack_channel'], task_id[0] + ' stuck in PvA pipeline')
                        self.restart('run',DAG_ID, task_id[0])
                        logging.info('Cleared and re ran the task')
                        # this is to resolve the connection timeout issue
                output = awk(awk(tail('-50', monitor_log ), "-F", " ", "{print $9}"),"-F","/","{print $7}")
                tasks = set()
                for task in output:
                    tasks.add(task)
                tasks.remove('\n')
                logging.info(tasks)
                if len(tasks) == 0:
                    logging.info('Pipeline seems to be stuck, executed backfill')
                    self.restart('backfill', DAG_ID)



user = os.path.expanduser('~').replace('/home/','')
projects = ['test_project']
base_log_folder='/home/'+user+'/logs/'
for project in projects:
    dag_id = str(user) + project
    if not os.path.exists(base_log_folder+dag_id):
        os.makedirs(base_log_folder+dag_id)
    log_dir = base_log_folder+dag_id +'/'
    monitor = JobMonitor()
    monitor.job_monitor(dag_id,log_dir)
