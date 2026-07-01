from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.insert(0, '/home/batman/airflow_f1/scripts')

from extract import extract
from transform import transform
from load import load

with DAG(
    dag_id='f1_etl_pipeline',
    start_date=datetime(2026, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['f1', 'etl']
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load
    )

    extract_task >> transform_task >> load_task
