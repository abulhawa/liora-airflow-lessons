import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="sensor_dag",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["tutorial"],
) as dag:

    my_sensor = FileSensor(
        task_id="check_file",
        fs_conn_id="my_filesystem_connection",
        filepath="my_file.txt",
        poke_interval=30,
        timeout=150,
        mode="reschedule",
    )

    my_task = BashOperator(
        task_id="print_file_content",
        bash_command="cat /tmp/my_file.txt",
    )

    my_sensor >> my_task
