# Airflow Worker Monitor

The script keeps checking for celeryd worker processes every minute scheduled through cron.

If there are no workers found the script starts the airflow workers.
