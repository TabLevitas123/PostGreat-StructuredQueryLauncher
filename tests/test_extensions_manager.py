
import unittest
from database.extensions_manager import ExtensionsManager
from database.connection_manager import ConnectionManager

class TestExtensionsManager(unittest.TestCase):
    def setUp(self):
        # Initialize the ExtensionsManager and ConnectionManager instances
        self.extensions_manager = ExtensionsManager()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Define a test extension (using the "uuid-ossp" extension for testing)
        self.extension_name = "uuid-ossp"

    def test_enable_extension(self):
        self.extensions_manager.enable_extension(self.extension_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT extname FROM pg_extension WHERE extname = %s;", (self.extension_name,))
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], self.extension_name)

    def test_disable_extension(self):
        self.extensions_manager.enable_extension(self.extension_name)
        self.extensions_manager.disable_extension(self.extension_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT extname FROM pg_extension WHERE extname = %s;", (self.extension_name,))
            result = cursor.fetchone()
            self.assertIsNone(result)

    def tearDown(self):
        # Ensure the extension is disabled if it exists
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP EXTENSION IF EXISTS {self.extension_name};")
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
