from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# from spotify_etl import run_spotify_etl

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 11, 8),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG(
    "minimium_dag",
    default_args=default_args,
    description="Our first DAG with ETL process!",
    schedule=timedelta(days=1),
)


def just_a_function():
    print("I'm going to show you something :)")


run_etl = PythonOperator(
    task_id="whole_spotify_etl",
    python_callable=just_a_function,
    dag=dag,
)

run_etl
