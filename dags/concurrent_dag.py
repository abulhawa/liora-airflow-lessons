
import time
import pendulum

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def wait_1_minute():
    time.sleep(60)


with DAG(
    dag_id="concurrent_dag",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["tutorial", "pools"],
    default_args={
        "pool": "micro_pool"
    },
) as dag:

    task1 = PythonOperator(
        task_id="wait1",
        python_callable=wait_1_minute,
    )

    task2 = PythonOperator(
        task_id="wait2",
        python_callable=wait_1_minute,
    )

    task3 = PythonOperator(
        task_id="wait3",
        python_callable=wait_1_minute,
    )

    # No dependencies: all three tasks can run independently.
