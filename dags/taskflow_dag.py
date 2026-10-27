import pendulum
from airflow.sdk import dag, task

@dag(
    dag_id="taskflow_example",
    start_date=pendulum.datetime(2026, 10, 1, tz="UTC"),
    schedule=None,
    catchup=False,
)
def my_pipeline():

    @task
    def calculate_score():
        return 0.92

    @task
    def check_score(score):
        print(f"Model score: {score}")

    check_score(calculate_score())

my_pipeline()