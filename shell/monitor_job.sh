#!/bin/bash

execution_date=`date +%Y-%m-%d`

# activate virtual-env
source /home/siyer/virtualenv/airflow/bin/activate


function clear_n_run() {
        airflow clear -t $1 -s $execution_date -e $execution_date -c $2
        sleep 5
        # Running jobs when cleared goes into shutdown state, the next clear, clears that too.
        airflow clear -t $1 -s $execution_date -e $execution_date -c $2
        sleep 10
        # start the job
        airflow run $2 $1 $execution_date
}


function backfill() {
        airflow backfill $2 -s $execution_date -e $execution_date
}

$@
