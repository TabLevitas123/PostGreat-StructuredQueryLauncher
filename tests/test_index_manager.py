
import unittest
from database.index_manager import IndexManager
from database.connection_manager import ConnectionManager
from database.table_manager import TableManager

class TestIndexManager(unittest.TestCase):
    def setUp(self):
        # Initialize the IndexManager and TableManager instances
        self.index_manager = IndexManager()
        self.table_manager = TableManager()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Define a test schema, table, and columns
        self.schema_name = "test_schema"
        self.table_name = f"{self.schema_name}.test_table"
        self.index_name = "test_index"
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.schema_name};")
        self.table_manager.create_table(self.table_name, {"id": "SERIAL PRIMARY KEY", "name": "VARCHAR(100)"})

    def test_create_index(self):
        columns = ["name"]
        self.index_manager.create_index(self.index_name, self.table_name, columns)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT indexname FROM pg_indexes WHERE tablename = 'test_table';")
            result = cursor.fetchall()
            self.assertTrue(any(self.index_name in idx[0] for idx in result))

    def test_drop_index(self):
        columns = ["name"]
        self.index_manager.create_index(self.index_name, self.table_name, columns)
        self.index_manager.drop_index(self.index_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT indexname FROM pg_indexes WHERE tablename = 'test_table';")
            result = cursor.fetchall()
            self.assertFalse(any(self.index_name in idx[0] for idx in result))

    def tearDown(self):
        # Drop the test schema and close connection
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP SCHEMA IF EXISTS {self.schema_name} CASCADE;")
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
