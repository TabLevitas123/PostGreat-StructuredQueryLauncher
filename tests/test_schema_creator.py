
import unittest
from database.schema_creator import SchemaCreator
from database.connection_manager import ConnectionManager

class TestSchemaCreator(unittest.TestCase):
    def setUp(self):
        # Initialize the SchemaCreator instance
        self.schema_creator = SchemaCreator()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

    def test_create_schema(self):
        schema_name = "test_schema"
        self.schema_creator.create_schema(schema_name)
        
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = %s", (schema_name,))
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], schema_name)

    def test_delete_schema(self):
        schema_name = "test_schema"
        self.schema_creator.create_schema(schema_name)
        self.schema_creator.delete_schema(schema_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = %s", (schema_name,))
            result = cursor.fetchone()
            self.assertIsNone(result)

    def tearDown(self):
        self.schema_creator.delete_schema("test_schema")
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
