import psycopg2
import os.path
import logging
import sh
import subprocess
from datetime import datetime, timedelta, date
from urlparse import urlparse
from airflow import configuration


class Delay_Detector:

    home_dir = os.path.expanduser('~')
    current_date = date.today()
    yesterday = date.today() - timedelta(1)
    last_week_date = date.today() - timedelta(8)
    ignore_tasks = ('test', '_start', 'monitor', 'done')

    def __init__(self,dag_id,task_id):
        self.dag_id = dag_id
        self.task_id = task_id

    def xstr(self, password):
        return str(password or '')

    def getDBConnection(self):
        sql_alchemy_conn = os.path.expanduser(configuration.get('core', 'SQL_ALCHEMY_CONN'))
        conn = urlparse(sql_alchemy_conn)
        db_name = conn.path[1:]
        user_name = conn.username
        host_name = conn.hostname
        pswd = self.xstr(conn.password)
        try:
            db_conn = psycopg2.connect('dbname=' + db_name + ' user=' + user_name + ' host=' + host_name + ' password=' + pswd)
            logging.info('Database connection acquired')
        except:
            logging.error('Unable to connect to the database')

        return db_conn.cursor()

    def notify(self,eta):
        send_notification = 'sh ' + self.home_dir + '/scripts/send_delay_notification.sh ' + eta
        subprocess.call(send_notification.split(), shell=False)

    def estimate(self):
        cur = self.getDBConnection()
        TABLEAU_REFRESH = 1
        # get list of tasks that ran for maximum duration (max duration will be calculated for parallel tasks run)
        cur.execute('SELECT task_id FROM task_instance WHERE duration IN (SELECT MAX(duration) FROM task_instance WHERE dag_id = %(DAG_ID)s AND DATE(execution_date) = %(YESTERDAY)s AND task_id NOT IN %(IGNORE_TASKS)s GROUP BY to_char(start_date, \'HH:MI\'))' ,{'DAG_ID': self.dag_id , 'YESTERDAY':self.yesterday.isoformat(),'IGNORE_TASKS':self.ignore_tasks})
        all_task_list = [task[0] for task in cur.fetchall()]
        # this query will get all the tasks that were run yesterday in ascending order
        #cur.execute('SELECT task_id FROM task_instance WHERE execution_date = %(EXECUTION_DATE)s AND dag_id = %(DAG_ID)s AND task_id NOT IN %(IGNORE_TASKS)s ORDER BY start_date ASC', {'EXECUTION_DATE': self.yesterday.isoformat() + ' 00:00:00','DAG_ID': self.dag_id, 'IGNORE_TASKS':self.ignore_tasks})
        #all_task_list = [task[0] for task in cur.fetchall()]
        logging.info('all_task_list: '  + str(all_task_list))
        # query to find all the completed task instances
        cur.execute('SELECT task_id FROM task_instance WHERE execution_date = %(EXECUTION_DATE)s AND dag_id = %(DAG_ID)s AND state = %(STATE)s', {'EXECUTION_DATE': self.current_date.isoformat() + ' 00:00:00','DAG_ID': self.dag_id, 'STATE':'success'})
        completed_tasks = [task[0] for task in cur.fetchall()]
        logging.info('completed_tasks: ' + str(completed_tasks))
        #completed_tasks = ['oline_ad_mapping','pva_final_quarterly_wide','pva_pre_final','slingshot_pre_final']
        # get the tasks that are yet to run
        pending_tasks = tuple([task for task in all_task_list if task not in completed_tasks])
        logging.info('pending_tasks: '+ str(pending_tasks))
        cur.execute('SELECT SUM(avg_run_time) FROM (SELECT AVG(duration) / 60 AS avg_run_time FROM task_instance WHERE dag_id = %(DAG_ID)s AND DATE(execution_date) BETWEEN %(LAST_WEEK_DATE)s AND %(YESTERDAY)s AND task_id IN %(PENDING_TASKS)s GROUP BY task_id) inner_query', {'DAG_ID': self.dag_id,'YESTERDAY':self.yesterday.isoformat(), 'LAST_WEEK_DATE':self.last_week_date.isoformat(),'PENDING_TASKS': pending_tasks})
        minutes = cur.fetchone()[0]
        estimated_completion_time = '{:02}:{:02}'.format(*divmod(int(minutes), 60))
        time_remaining = datetime.strptime(estimated_completion_time, '%H:%M').time()
        eta = datetime.now() + timedelta(hours=time_remaining.hour+TABLEAU_REFRESH, minutes=time_remaining.minute)
        return eta.strftime('%H:%M')


    def check_run_time(self):
        cur = self.getDBConnection()
        cur.execute('SELECT state FROM  task_instance WHERE execution_date = %(EXECUTION_DATE)s AND dag_id = %(DAG_ID)s AND task_id = %(TASK_ID)s', {'EXECUTION_DATE': self.current_date.isoformat() + ' 00:00:00','DAG_ID': self.dag_id,'TASK_ID': self.task_id})
        logging.info('hello'  + str(cur.rowcount) )
        if cur.rowcount == 1:
            eta = self.estimate()
            self.notify(eta)
            #logging.info('Sending notification')
        else:
            state = cur.fetchone()[0]
            if state == 'success':
                logging.info(self.task_id + ' completed in time')
            else:
                logging.info('Sending notification')
        cur.close()

user = sh.whoami()
project = 'test_project'
dag_id = str(user)[:-1]+project
task_id = 'test_task
dd = Delay_Detector(dag_id,task_id)
dd.check_run_time()
