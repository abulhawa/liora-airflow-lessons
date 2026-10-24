import pendulum

from airflow.sdk import DAG
import time
from airflow.providers.standard.operators.python import PythonOperator


def print_date_and_hello():
    print(pendulum.now("Europe/Berlin"))
    print("Scheduling with Airflow")


with DAG(
    dag_id="scheduled_dag",
    description="Trying schedules in Airflow dags",
    start_date=pendulum.datetime(2026, 10, 1, tz="Europe/Berlin"),
    schedule='* * * * *',
    catchup=False,
    tags=["Ali", "tutorial"],
) as dag:

    task = PythonOperator(
        task_id="print_current_date_time",
        python_callable=print_date_and_hello,
    )
