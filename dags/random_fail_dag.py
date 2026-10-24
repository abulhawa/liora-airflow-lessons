import random
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

def successful_task():
    print("Task succeeded")

def random_fail_task():
    value = random.random()
    print(f"Random value: {value}")

    if value < 0.9:
        raise Exception("Random failure!")
    
with DAG(
    dag_id='randomly_failing_dag',
    schedule=None,
    catchup=False,
) as _:
    
    task1 = PythonOperator(
        task_id="task1",
        python_callable=random_fail_task,
    )
    
    task2 = PythonOperator(
        task_id="task2",
        python_callable=successful_task,
        trigger_rule="one_failed",
    )
    
    task3 = PythonOperator(
        task_id="task3",
        python_callable=successful_task,
        trigger_rule="one_success",
    )
    
    task4 = PythonOperator(
        task_id="task4",
        python_callable=successful_task,
        trigger_rule="all_done",
    )
    
    task1 >> [task2, task3] >> task4