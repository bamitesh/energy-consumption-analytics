# magefile.py

from mage import task

@task
def run_example_job():
    from src.jobs.example_job import ExampleJob
    job = ExampleJob()
    job.run()

@task
def initialize_database():
    from backend.database.init_duckdb import initialize
    initialize()

@task
def run_all():
    run_example_job()
    initialize_database()