from duckdb import connect

def init_duckdb(db_path='database.duckdb'):
    # Connect to DuckDB database
    conn = connect(db_path)

    # Create a sample table
    conn.execute("""
    CREATE TABLE IF NOT EXISTS example_table (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        value FLOAT
    )
    """)

    # Insert initial data
    conn.execute("""
    INSERT INTO example_table (id, name, value) VALUES
    (1, 'Sample A', 10.0),
    (2, 'Sample B', 20.0)
    """)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_duckdb()