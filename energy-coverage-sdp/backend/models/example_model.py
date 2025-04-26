class ExampleModel:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id INTEGER PRIMARY KEY,
            name TEXT,
            value FLOAT
        );
        """
        self.db_connection.execute(query)

    def insert_data(self, name, value):
        query = "INSERT INTO example_table (name, value) VALUES (?, ?);"
        self.db_connection.execute(query, (name, value))

    def fetch_data(self):
        query = "SELECT * FROM example_table;"
        return self.db_connection.execute(query).fetchall()