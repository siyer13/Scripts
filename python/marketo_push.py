#!/usr/bin/python

from marketorestpython.client import MarketoClient
from psycopg2.extensions import AsIs
import psycopg2
import MySQLdb
import sys
import json
import logging
import datetime

now = datetime.datetime.now()
logfile = '/mnt1/user/logs/marketo-'+ now.strftime("%Y-%m-%d") + '.log'

logging.basicConfig(filename=logfile,level=logging.DEBUG)

con = None

munchkin_id = "xxxx"
client_id = "xxxxx"
client_secret= "xxxxx"
mc = MarketoClient(munchkin_id, client_id, client_secret)


redshift_connection_parameters = {
        'host': 'xxxxx',
        'port': 5439,
        'database': 'xxxx',
        'user': 'xxxx',
        'password': 'xxxx'
    }

mysql_connection_parameters = {
        'host': 'xxxxxx',
        'port': 3306,
        'db': 'xxx',
        'user': 'xxxx',
        'passwd': 'xx'
    }

columns =  ('email',
            'firstName',
            'lastName',
            'company',
            'phone',
            'country',
            'title',
            'postalCode',
            'state',
            'city',
            'unsubscribed',
            'twitterId'
           )

try:

    redshift_con = psycopg2.connect(**redshift_connection_parameters)
    mysql_con = MySQLdb.connect(**mysql_connection_parameters)

    redshift_cursor = redshift_con.cursor()

    mysql_cursor = mysql_con.cursor()
    redshift_cursor.execute('SELECT COUNT(*) FROM public.marketo')
    no_of_records = redshift_cursor.fetchone()[0]
    print no_of_records
    for offset in xrange(0,no_of_records,300):
        print 'OFFSET', offset
        redshift_cursor.execute("SELECT * FROM public.marketo ORDER BY firstname LIMIT 300 OFFSET {0}".format(offset))

        leads = []
        for row in redshift_cursor.fetchall():

            leads.append(dict(zip(columns, row)))

        logging.debug(json.dumps(leads, indent=2))
        lead = mc.execute(method='create_update_leads', leads=leads, action='createOrUpdate', lookupField='email',
                    asyncProcessing='false', partitionName='Default')
        logging.info(lead)
        marketo_response = json.loads(json.dumps(lead))
        for key in marketo_response:
            if key['status'] == 'updated' or key['status'] == 'created':
                print key['status'], "and", key['id']
                mysql_cursor.execute("""INSERT INTO marketo_response (status, message) values ("{0}","{1}") """.format(key['status'],key['id']))
                mysql_con.commit()
            elif key['status'] == 'skipped':
                mysql_cursor.execute("""INSERT INTO marketo_response values ("{0}","{1}","{2}") """.format(key['status'],key['reasons'][0]['message'],key['reasons'][0]['code']))
                mysql_con.commit()
        logging.info('Marketo response inserted to mysql')
        logging.info('******* Process completed.')

except psycopg2.DatabaseError, e:
    logging.error('******** Connection Error')
    logging.error('Error %s' % e)
    sys.exit(1)
except MySQLdb.Error, e:
    logging.error('******** Connection Error')
    logging.error('Error %s' % e)
    print e
    sys.exit(1)
except Exception as e:
    logging.error(e)

finally:

    if redshift_con:
        redshift_con.close()
    if mysql_con:
        mysql_con.close()
