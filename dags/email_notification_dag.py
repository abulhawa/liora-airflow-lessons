
from datetime import timedelta

import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def failed_task():
    raise Exception("Intentional failure for email testing")


with DAG(
    dag_id="email_notification_dag",
    description="Testing email alerts",
    start_date=pendulum.datetime(2026, 10, 1, tz="Europe/Berlin"),
    schedule=None,
    catchup=False,
    tags=["tutorial", "notifications"],
) as dag:

    task1 = PythonOperator(
        task_id="my_failed_task",
        python_callable=failed_task,
        retries=5,
        retry_delay=timedelta(seconds=30),
        email=["your-email@example.com"],
        email_on_retry=True,
        email_on_failure=True,
    )
