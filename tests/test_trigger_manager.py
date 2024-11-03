
import unittest
from database.trigger_manager import TriggerManager
from database.table_manager import TableManager
from database.connection_manager import ConnectionManager

class TestTriggerManager(unittest.TestCase):
    def setUp(self):
        # Initialize the TriggerManager, TableManager, and ConnectionManager
        self.trigger_manager = TriggerManager()
        self.table_manager = TableManager()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Define a test schema, table, and trigger
        self.schema_name = "test_schema"
        self.table_name = f"{self.schema_name}.test_table"
        self.trigger_name = "test_trigger"
        self.function_name = "test_function"

        # Set up the test schema, table, and function
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.schema_name};")
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (id SERIAL PRIMARY KEY, name VARCHAR(100));")
            cursor.execute(f"CREATE OR REPLACE FUNCTION {self.function_name}() RETURNS TRIGGER AS $$ "
                           f"BEGIN RETURN NEW; END; $$ LANGUAGE plpgsql;")

    def test_create_trigger(self):
        self.trigger_manager.create_trigger(self.trigger_name, self.table_name, "BEFORE", "INSERT", self.function_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT tgname FROM pg_trigger WHERE tgname = %s;", (self.trigger_name,))
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], self.trigger_name)

    def test_enable_trigger(self):
        self.trigger_manager.create_trigger(self.trigger_name, self.table_name, "BEFORE", "INSERT", self.function_name)
        self.trigger_manager.disable_trigger(self.trigger_name, self.table_name)
        self.trigger_manager.enable_trigger(self.trigger_name, self.table_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT tgname FROM pg_trigger WHERE tgname = %s AND tgenabled = 'O';", (self.trigger_name,))
            result = cursor.fetchone()
            self.assertIsNotNone(result)

    def test_disable_trigger(self):
        self.trigger_manager.create_trigger(self.trigger_name, self.table_name, "BEFORE", "INSERT", self.function_name)
        self.trigger_manager.disable_trigger(self.trigger_name, self.table_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT tgname FROM pg_trigger WHERE tgname = %s AND tgenabled = 'D';", (self.trigger_name,))
            result = cursor.fetchone()
            self.assertIsNotNone(result)

    def test_drop_trigger(self):
        self.trigger_manager.create_trigger(self.trigger_name, self.table_name, "BEFORE", "INSERT", self.function_name)
        self.trigger_manager.drop_trigger(self.trigger_name, self.table_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT tgname FROM pg_trigger WHERE tgname = %s;", (self.trigger_name,))
            result = cursor.fetchone()
            self.assertIsNone(result)

    def tearDown(self):
        # Drop the test schema and close connection
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP SCHEMA IF EXISTS {self.schema_name} CASCADE;")
            cursor.execute(f"DROP FUNCTION IF EXISTS {self.function_name}();")
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
