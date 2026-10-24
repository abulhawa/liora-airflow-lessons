import pendulum

from airflow.sdk import DAG
import time
from airflow.providers.standard.operators.python import PythonOperator


def print_date_and_hello():
    print(pendulum.now("Europe/Berlin"))
    print("Hello from Airflow")


with DAG(
    dag_id="my_very_first_dag",
    description="My first Airflow DAG",
    start_date=pendulum.datetime(2026, 10, 1, tz="Europe/Berlin"),
    schedule=None,
    catchup=False,
    tags=["tutorial"],
) as dag:

    first_task = PythonOperator(
        task_id="print_hello",
        python_callable=print_date_and_hello,
    )
    
    second_task = PythonOperator(
    task_id="print_again",
    python_callable=print_date_and_hello,
    )
    
    first_task << second_task
