from pyspark.sql import SparkSession
from src.jobs.example_job import ExampleJob

def main():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("Python PySpark Project") \
        .getOrCreate()

    # Create an instance of ExampleJob
    job = ExampleJob(spark)

    # Run the job
    job.run()

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()