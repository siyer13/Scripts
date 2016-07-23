#connecting to mysql with python using pymysql
# pymysql is purely written in python with no external dependencies

import pymysql.cursors
import logging.config
import yaml

with open('logging.yaml') as f:
    D = yaml.load(f)
    D.setdefault('version', 1)
    logging.config.dictConfig(D)


logger = logging.getLogger('my_module')
connection = pymysql.connect(host='localhost',user='root',password='password',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
connection.select_db('employee')
cursor.execute("SELECT * FROM ADDRESS")
result = cursor.fetchall()
logger.error(result)
cursor.close()
