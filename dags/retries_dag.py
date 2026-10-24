
from datetime import timedelta

import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def failed_task():
    raise Exception("This task did not work!")


with DAG(
    dag_id="retries_dag",
    description="Testing automatic retries",
    start_date=pendulum.datetime(2026, 10, 1, tz="Europe/Berlin"),
    schedule=None,
    catchup=False,
    tags=["tutorial", "retries"],
) as dag:

    task1 = PythonOperator(
        task_id="my_failed_task",
        python_callable=failed_task,
        retries=5,
        retry_delay=timedelta(seconds=30),
    )
