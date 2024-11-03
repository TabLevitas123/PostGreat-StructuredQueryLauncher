
import unittest
from database.connection_manager import ConnectionManager
from psycopg2 import OperationalError

class TestConnectionManager(unittest.TestCase):
    def setUp(self):
        # Initialize the ConnectionManager instance
        self.conn_manager = ConnectionManager()

    def test_connection_failure(self):
        # Test connection failure with incorrect details
        self.conn_manager.config.set("host", "invalid_host")
        with self.assertRaises(OperationalError):
            self.conn_manager.connect()

    def test_connection_and_closing(self):
        # Test successful connection and closing
        self.conn_manager.config.set("host", "localhost")  # Assume localhost for testing
        self.conn_manager.config.set("user", "test_user")
        self.conn_manager.config.set("password", "test_password")
        self.conn_manager.config.set("database", "test_db")

        try:
            self.conn_manager.connect()
            self.assertIsNotNone(self.conn_manager.connection)
        finally:
            self.conn_manager.close_connection()
            self.assertIsNone(self.conn_manager.connection)

    def tearDown(self):
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
