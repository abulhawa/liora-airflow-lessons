import pendulum
from airflow.sdk import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
    dag_id="hello_world",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["docker", "liora"],
) as dag:

    hello_world = DockerOperator(
        task_id="hello_world",
        image="hello-world",
        docker_url="unix://var/run/docker.sock",
        mount_tmp_dir=False,
        auto_remove="never",
    )