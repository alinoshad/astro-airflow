from airflow import DAG
from airflow.operators.empty import EmptyOperator

from datetime import datetime

default_args = {
    'owner': 'awais',
    'start_date': datetime(2023, 8, 1),
    'retries': 1,
}

dag = DAG(
    dag_id="my_first_dag_b6",
    default_args=default_args,
    schedule_interval=None)

task_1 = EmptyOperator(
    task_id = "ui_task_1",
    dag=dag,
)

task_2 = EmptyOperator(
    task_id = "ui_task_2",
    dag=dag,
)
task_3 = EmptyOperator(
    task_id = "ui_task_3",
    dag=dag,
)

task_4 = EmptyOperator(
    task_id = "ui_task_4",
    dag=dag,
)

task_1 >> [task_2, task_3]
[task_2, task_3] >> task_4

