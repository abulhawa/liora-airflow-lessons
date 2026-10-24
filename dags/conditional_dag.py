
import pendulum

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


def successful_task():
    print("Task succeeded")


def failed_task():
    raise Exception("This task deliberately failed!")


with DAG(
    dag_id="conditional_dag",
    description="Testing task failures and trigger rules",
    start_date=pendulum.datetime(2026, 10, 1, tz="Europe/Berlin"),
    schedule=None,
    catchup=False,
    tags=["tutorial", "failures"],
) as dag:

    task1 = PythonOperator(
        task_id="task1",
        python_callable=successful_task,
    )

    task2 = PythonOperator(
        task_id="task2",
        python_callable=failed_task,
    )

    task3 = PythonOperator(
        task_id="task3",
        python_callable=successful_task,
        trigger_rule="all_done",
    )

    [task1, task2] >> task3
