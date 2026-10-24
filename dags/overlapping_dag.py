from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime
import pendulum

import time

def sleep_40_seconds():
    time.sleep(40)

with DAG(
    dag_id='too_long_dag',
    description="My DAG that's triggered every 10 seconds",
    tags=['tutorial', 'Ali'],
    schedule=datetime.timedelta(seconds=10),
    start_date=pendulum.datetime(2026, 10, 1, tz="Europe/Berlin"),
    catchup=False,
    max_active_runs=2,
) as my_dag:

    my_task = PythonOperator(
        task_id='sleep_40_seconds',
        python_callable=sleep_40_seconds
    )