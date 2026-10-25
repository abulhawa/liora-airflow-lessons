from airflow.sdk import DAG
from airflow.providers.standard.operators.python import BranchPythonOperator
from airflow.providers.standard.operators.empty import EmptyOperator


def choose_branch():
    accuracy = 0.92
    if accuracy >= 0.90:
        return "deploy"
    return "review"

decision = BranchPythonOperator(
    task_id="decision",
    python_callable=choose_branch,
)

with DAG(dag_id='branched_dag'):
    deploy= EmptyOperator(task_id="deploy")
    review= EmptyOperator(task_id="review")
    
    decision >> [deploy, review]