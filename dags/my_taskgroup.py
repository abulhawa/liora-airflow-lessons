from airflow.sdk import DAG, TaskGroup
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="task_group",
    schedule=None,
    tags=['tutorial', 'datascientest'],
    
) as my_dag:

    with TaskGroup("group_A") as group_A:
        task_A1 = EmptyOperator(task_id="task_A1")
        task_A2 = EmptyOperator(task_id="task_A2")
        task_A3 = EmptyOperator(task_id="task_A3")

    with TaskGroup("group_B") as group_B:
        task_B1 = EmptyOperator(task_id="task_B1")
        task_B2 = EmptyOperator(task_id="task_B2")

    with TaskGroup("group_C") as group_C:
        task_C1 = EmptyOperator(task_id="task_C1")
        task_C2 = EmptyOperator(task_id="task_C2")
        task_C3 = EmptyOperator(task_id="task_C3")

    start_task = EmptyOperator(task_id='start_task')
    end_task = EmptyOperator(task_id='end_task')

    start_task >> [group_A, group_B]
    [group_A, group_B] >> group_C >> end_task

