
import unittest
from database.type_manager import TypeManager
from database.connection_manager import ConnectionManager

class TestTypeManager(unittest.TestCase):
    def setUp(self):
        # Initialize the TypeManager and ConnectionManager instances
        self.type_manager = TypeManager()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Define a test ENUM type
        self.enum_type_name = "test_enum_type"
        self.enum_values = ["value1", "value2", "value3"]

    def test_create_enum_type(self):
        self.type_manager.create_enum_type(self.enum_type_name, self.enum_values)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT typname FROM pg_type WHERE typname = %s;", (self.enum_type_name,))
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], self.enum_type_name)

    def test_drop_type(self):
        self.type_manager.create_enum_type(self.enum_type_name, self.enum_values)
        self.type_manager.drop_type(self.enum_type_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT typname FROM pg_type WHERE typname = %s;", (self.enum_type_name,))
            result = cursor.fetchone()
            self.assertIsNone(result)

    def tearDown(self):
        # Ensure the type is dropped if it exists
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP TYPE IF EXISTS {self.enum_type_name};")
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
