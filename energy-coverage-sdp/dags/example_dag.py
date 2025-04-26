from mage import DAG
from mage.operators import PythonOperator
from src.jobs.example_job import ExampleJob

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': '2023-10-01',
    'retries': 1,
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='An example DAG for running a Spark job',
    schedule_interval='@daily',
)

def run_example_job():
    job = ExampleJob()
    job.run()

run_job_task = PythonOperator(
    task_id='run_example_job',
    python_callable=run_example_job,
    dag=dag,
)

run_job_task