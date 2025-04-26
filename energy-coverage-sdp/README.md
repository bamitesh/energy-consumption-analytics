# Python PySpark Project

This project is designed to leverage PySpark for data processing and orchestration using Mage, with DuckDB as the backend database. The project is structured to facilitate easy development, testing, and deployment.

## Project Structure

```
python-pyspark-project
├── src
│   ├── main.py                # Entry point of the application
│   ├── utils
│   │   └── helpers.py         # Utility functions for data processing and logging
│   └── jobs
│       └── example_job.py     # Example job logic for Spark execution
├── dags
│   └── example_dag.py         # DAG definition for orchestrating workflows with Mage
├── backend
│   ├── models
│   │   └── example_model.py    # Model definition for interacting with DuckDB
│   └── database
│       └── init_duckdb.py     # Initialization logic for DuckDB database
├── docker
│   ├── Dockerfile              # Instructions for building the Docker image
│   └── docker-compose.yml      # Configuration for running the application in Docker
├── .github
│   └── workflows
│       └── deploy.yml          # GitHub Actions workflow for deploying to AWS
├── requirements.txt            # List of Python dependencies
├── magefile.py                 # Mage orchestration tasks
├── README.md                   # Project documentation
└── .gitignore                  # Files and directories to ignore by Git
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd python-pyspark-project
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Initialize DuckDB:**
   Run the initialization script to set up the database:
   ```
   python backend/database/init_duckdb.py
   ```

4. **Run the application:**
   Execute the main script to start the application:
   ```
   python src/main.py
   ```

## Usage

- To run a specific job, you can invoke it from the `src/jobs/example_job.py` file.
- The DAG defined in `dags/example_dag.py` can be used to orchestrate workflows using Mage.

## Deployment

The project is configured for deployment using GitHub Actions. The workflow file located at `.github/workflows/deploy.yml` contains the necessary steps for building, testing, and deploying the application to AWS.

## Examples

Refer to the individual files in the `src/jobs` and `backend/models` directories for examples of job definitions and database interactions.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.