import pendulum

from airflow.sdk import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

with DAG(
    dag_id="create_table",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
) as dag:

    create_customer = SQLExecuteQueryOperator(
        task_id="create_customer",
        conn_id="postgres",
        sql="""
            CREATE TABLE IF NOT EXISTS customer (
                id UUID PRIMARY KEY,
                firstname VARCHAR(100),
                lastname VARCHAR(100)
            );
        """,
    )
