import pendulum

from airflow.sdk import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


with DAG(
    dag_id="init_order",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=['order', 'postgres', 'mle'],
) as dag:
    create_customer = SQLExecuteQueryOperator(
        task_id="create_customer",
        conn_id="postgres",
        sql="sql/create_table_customer.sql",
    )
    
    create_product = SQLExecuteQueryOperator(
        task_id="create_product",
        conn_id="postgres",
        sql="sql/create_table_product.sql",
    )
    
    create_order = SQLExecuteQueryOperator(
        task_id="create_order",
        conn_id="postgres",
        sql="sql/create_table_order.sql",
    )
    
    [create_product, create_customer] >> create_order
