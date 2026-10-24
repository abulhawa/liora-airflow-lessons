import pendulum
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

def print_text(text):
    print(text)
    
    
with DAG(
    dag_id="leaving_home_dag",
    description="start from gettings dressed",
    start_date=pendulum.datetime(2026, 10, 1, tz="Europe/Berlin"),
    schedule=None,
    catchup=False,
    tags=["tutorial", "Ali"],
) as dag:
        
    texts = [
        'Pulling on trousers',
        'Pull on right sock',
        'Pull on right shoe',
        'Pull on left sock',
        'Put on left shoe',
        'Take out',
    ]

    ids = [
        'trousers',
        'right_sock',
        'right_shoe',
        'left_sock',
        'left_shoe',
        'exit',
    ]
    
    tasks = {}
    
    for t, i in zip(texts, ids):
        tasks[i] = PythonOperator(
            task_id=i,
            python_callable=print_text,
            op_kwargs={"text": t},
        )
        
    tasks['exit'] << [tasks['left_shoe'], tasks['right_shoe']]
    tasks['trousers'] >> [tasks['right_sock'], tasks['left_sock']]
    tasks['right_sock'] >> tasks['right_shoe']
    tasks['left_sock'] >> tasks['left_shoe']

    
