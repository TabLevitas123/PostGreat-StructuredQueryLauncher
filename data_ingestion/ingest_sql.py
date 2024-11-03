
import psycopg2
from config import Config
from database.connection_manager import ConnectionManager

class SQLIngestor:
    def __init__(self, sql_file_path):
        self.sql_file_path = sql_file_path
        self.conn_manager = ConnectionManager()

    def execute_sql_file(self):
        with open(self.sql_file_path, mode="r", encoding="utf-8") as file:
            sql_commands = file.read()

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(sql_commands)
            self.conn_manager.connection.commit()
            print(f"SQL commands from {self.sql_file_path} executed successfully.")

if __name__ == "__main__":
    # Example usage
    sql_file_path = "your_sql_dump.sql"
    sql_ingestor = SQLIngestor(sql_file_path)
    sql_ingestor.execute_sql_file()
