
import unittest
from database.table_manager import TableManager
from database.connection_manager import ConnectionManager

class TestTableManager(unittest.TestCase):
    def setUp(self):
        # Initialize the TableManager instance
        self.table_manager = TableManager()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Define a test schema and table
        self.schema_name = "test_schema"
        self.table_name = f"{self.schema_name}.test_table"
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.schema_name};")

    def test_create_table(self):
        columns = {"id": "SERIAL PRIMARY KEY", "name": "VARCHAR(100)"}
        self.table_manager.create_table(self.table_name, columns)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = 'test_table';")
            result = cursor.fetchall()
            self.assertEqual(len(result), len(columns))
            self.assertEqual(result[0][0], "id")
            self.assertEqual(result[1][0], "name")

    def test_add_column(self):
        columns = {"id": "SERIAL PRIMARY KEY"}
        self.table_manager.create_table(self.table_name, columns)
        self.table_manager.add_column(self.table_name, "age", "INTEGER")

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'test_table' AND column_name = 'age';")
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], "age")

    def tearDown(self):
        # Drop the test schema and table
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP SCHEMA IF EXISTS {self.schema_name} CASCADE;")
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
