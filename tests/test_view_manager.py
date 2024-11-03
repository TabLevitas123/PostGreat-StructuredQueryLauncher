
import unittest
from database.view_manager import ViewManager
from database.connection_manager import ConnectionManager
from database.table_manager import TableManager

class TestViewManager(unittest.TestCase):
    def setUp(self):
        # Initialize the ViewManager and TableManager instances
        self.view_manager = ViewManager()
        self.table_manager = TableManager()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Define a test schema, table, and view
        self.schema_name = "test_schema"
        self.table_name = f"{self.schema_name}.test_table"
        self.view_name = f"{self.schema_name}.test_view"
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.schema_name};")
        self.table_manager.create_table(self.table_name, {"id": "SERIAL PRIMARY KEY", "name": "VARCHAR(100)"})

    def test_create_view(self):
        query = f"SELECT * FROM {self.table_name}"
        self.view_manager.create_view(self.view_name, query)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT table_name FROM information_schema.views WHERE table_name = 'test_view';")
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], "test_view")

    def test_create_materialized_view(self):
        query = f"SELECT * FROM {self.table_name}"
        self.view_manager.create_materialized_view(self.view_name, query)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT matviewname FROM pg_matviews WHERE matviewname = 'test_view';")
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], "test_view")

    def test_drop_view(self):
        query = f"SELECT * FROM {self.table_name}"
        self.view_manager.create_view(self.view_name, query)
        self.view_manager.drop_view(self.view_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT table_name FROM information_schema.views WHERE table_name = 'test_view';")
            result = cursor.fetchone()
            self.assertIsNone(result)

    def tearDown(self):
        # Drop the test schema and close connection
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP SCHEMA IF EXISTS {self.schema_name} CASCADE;")
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
