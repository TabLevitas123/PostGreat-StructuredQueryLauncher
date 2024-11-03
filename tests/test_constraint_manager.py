
import unittest
from database.constraint_manager import ConstraintManager
from database.table_manager import TableManager
from database.connection_manager import ConnectionManager

class TestConstraintManager(unittest.TestCase):
    def setUp(self):
        # Initialize the ConstraintManager, TableManager, and ConnectionManager
        self.constraint_manager = ConstraintManager()
        self.table_manager = TableManager()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Define a test schema, table, and columns
        self.schema_name = "test_schema"
        self.table_name = f"{self.schema_name}.test_table"
        self.ref_table_name = f"{self.schema_name}.ref_table"
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.schema_name};")
        self.table_manager.create_table(self.table_name, {"id": "SERIAL PRIMARY KEY", "name": "VARCHAR(100)"})
        self.table_manager.create_table(self.ref_table_name, {"id": "SERIAL PRIMARY KEY"})

    def test_add_primary_key(self):
        self.constraint_manager.add_primary_key(self.table_name, "id")
        
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT constraint_name FROM information_schema.table_constraints WHERE table_name = 'test_table' AND constraint_type = 'PRIMARY KEY';")
            result = cursor.fetchone()
            self.assertIsNotNone(result)

    def test_add_foreign_key(self):
        self.constraint_manager.add_foreign_key(self.table_name, "name", self.ref_table_name, "id")

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT constraint_name FROM information_schema.table_constraints WHERE table_name = 'test_table' AND constraint_type = 'FOREIGN KEY';")
            result = cursor.fetchone()
            self.assertIsNotNone(result)

    def test_add_unique_constraint(self):
        self.constraint_manager.add_unique_constraint(self.table_name, "name")

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT constraint_name FROM information_schema.table_constraints WHERE table_name = 'test_table' AND constraint_type = 'UNIQUE';")
            result = cursor.fetchone()
            self.assertIsNotNone(result)

    def test_add_check_constraint(self):
        condition = "id > 0"
        self.constraint_manager.add_check_constraint(self.table_name, "check_id_positive", condition)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT constraint_name FROM information_schema.table_constraints WHERE table_name = 'test_table' AND constraint_type = 'CHECK';")
            result = cursor.fetchone()
            self.assertIsNotNone(result)

    def tearDown(self):
        # Drop the test schema and close connection
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP SCHEMA IF EXISTS {self.schema_name} CASCADE;")
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
