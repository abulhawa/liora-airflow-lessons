
import random

import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def successful_task():
    print("Task succeeded")


def random_fail_task():
    value = random.random()
    print(f"Random value: {value}")

    if value < 0.9:
        raise Exception("Task randomly failed")


def cleanup():
    print("Cleaning up resources")


with DAG(
    dag_id="setup_teardown_dag",
    description="Testing setup and teardown",
    start_date=pendulum.datetime(2026, 10, 1, tz="Europe/Berlin"),
    schedule=None,
    catchup=False,
    tags=["tutorial", "setup-teardown"],
) as dag:

    task1 = PythonOperator(
        task_id="setup",
        python_callable=successful_task,
    )

    task2 = PythonOperator(
        task_id="processing_A",
        python_callable=random_fail_task,
    )

    task3 = PythonOperator(
        task_id="processing_B",
        python_callable=random_fail_task,
    )

    task4 = PythonOperator(
        task_id="teardown",
        python_callable=cleanup,
    )

    task1.as_setup() >> [task2, task3]
    [task2, task3] >> task4.as_teardown()
