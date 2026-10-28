import pendulum

from airflow.sdk import DAG
from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.providers.standard.operators.python import PythonOperator

from docker.types import Mount

with DAG(
    dag_id="load_order",
    start_date=pendulum.datetime(2026, 10, 1, tz="Europe/Berlin"),
    schedule="0 17 * * *",
    catchup=False,
    tags=["orders", "docker", "postgres"],
) as dag:
    orders_sensor = FileSensor(
        task_id="orders_sensor",
        fs_conn_id="fs_default",
        filepath="data/to_ingest/bronze/orders.json",
    )

    python_transform = DockerOperator(
        task_id="python_transform",
        image="python_transform:latest",
        docker_url="unix://var/run/docker.sock",
        mount_tmp_dir=False,
        auto_remove="success",
        command="python3 main.py",
        network_mode="airflow_dst_default",
        mounts=[
            Mount(
                source="/home/ubuntu/airflow_dst/data/to_ingest",
                target="/app/data/to_ingest",
                type="bind",
            )
        ],
    )

    python_load = DockerOperator(
        task_id="python_load",
        image="python_load:latest",
        docker_url="unix://var/run/docker.sock",
        mount_tmp_dir=False,
        auto_remove="success",
        command="python3 main.py",
        environment={
            "HOST": "postgres",
            "DATABASE": "airflow",
            "USER": "airflow",
            "PASSWORD": "airflow",
        },
        network_mode="airflow_dst_default",
        mounts=[
            Mount(
                source="/home/ubuntu/airflow_dst/data/to_ingest",
                target="/app/data/to_ingest",
                type="bind",
            )
        ],
    )

    orders_sensor >> python_transform >> python_load
