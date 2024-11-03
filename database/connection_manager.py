
import psycopg2
from config import Config
from constants import ERROR_MESSAGES

class ConnectionManager:
    def __init__(self):
        self.config = Config()
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.config.get("host"),
                port=self.config.get("port"),
                user=self.config.get("user"),
                password=self.config.get("password"),
                database=self.config.get("database")
            )
            print("Connected to the database successfully.")
        except psycopg2.OperationalError as e:
            print(ERROR_MESSAGES["CONNECTION_FAILURE"], e)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def reconnect(self):
        self.close_connection()
        self.connect()

    def get_cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            raise ConnectionError(ERROR_MESSAGES["CONNECTION_FAILURE"])

    def __enter__(self):
        self.connect()
        return self.get_cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()
