#!/bin/sh
#
# SCRIPT: airflow_worker_monitor
# AUTHOR: siyer
# DATE: 2017-01-26
# REV: 0.1.T (Valid are A, B, D, T and P)
# (For Alpha, Beta, Dev, Test and Production)
#
# The script will check if airflow workers are running for
# the specific user. If not found, it will start the workers.

AIRFLOW_HOME=$HOME/airflow
AIRFLOW_VENV=$AIRFLOW_HOME/venv/bin

count=`ps -ef | grep celeryd | grep $(whoami) | wc -l`

if [ $count -le 1 ]
then
    source $AIRFLOW/activate
    nohup airflow worker& >> $AIRFLOW_HOME/logs/worker.log
    echo "$(date) INFO: Airflow workers started" >> /home/siyer/planned-vs-actual/cron.log
fi
