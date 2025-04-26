def log_message(message: str) -> None:
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def process_data(data) -> list:
    """Processes the input data and returns a list."""
    # Example processing logic
    return [item for item in data if item is not None]

def save_to_database(data, db_connection) -> None:
    """Saves the processed data to the database."""
    # Example logic to save data
    db_connection.execute("INSERT INTO table_name (column) VALUES (?)", (data,))