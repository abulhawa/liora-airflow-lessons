from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
import random


def function_with_return_unnamed():
    return random.uniform(a=0, b=1)

def function_with_return(task_instance):
    task_instance.xcom_push(
        key="my_xcom_value",
        value=random.uniform(a=0, b=1)
    )

with DAG(
    dag_id='xcom_dag',
    schedule=None,
    tags=['tutorial', 'datascientest'],
) as dag:

    my_task = PythonOperator(
        task_id='push_Xcom_Value',
        python_callable=function_with_return
    )
    
    def read_data_from_xcom(task_instance):
        print(
            task_instance.xcom_pull(
                key="my_xcom_value",
                task_ids=['python_task']
            )
        )


    my_task2 = PythonOperator(
        task_id="read_Xcom_value",
        python_callable=read_data_from_xcom
    )

    my_task >> my_task2