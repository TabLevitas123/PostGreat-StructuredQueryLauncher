
import unittest
from database.sequence_manager import SequenceManager
from database.connection_manager import ConnectionManager

class TestSequenceManager(unittest.TestCase):
    def setUp(self):
        # Initialize the SequenceManager and ConnectionManager instances
        self.sequence_manager = SequenceManager()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Define a test sequence
        self.sequence_name = "test_sequence"

    def test_create_sequence(self):
        self.sequence_manager.create_sequence(self.sequence_name, start=1, increment=1)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT sequence_name FROM information_schema.sequences WHERE sequence_name = %s", (self.sequence_name,))
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], self.sequence_name)

    def test_alter_sequence(self):
        self.sequence_manager.create_sequence(self.sequence_name, start=1, increment=1)
        self.sequence_manager.alter_sequence(self.sequence_name, increment=2)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"SELECT increment_by FROM pg_sequences WHERE schemaname = 'public' AND sequencename = '{self.sequence_name}';")
            result = cursor.fetchone()
            self.assertEqual(result[0], 2)

    def test_drop_sequence(self):
        self.sequence_manager.create_sequence(self.sequence_name, start=1, increment=1)
        self.sequence_manager.drop_sequence(self.sequence_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT sequence_name FROM information_schema.sequences WHERE sequence_name = %s", (self.sequence_name,))
            result = cursor.fetchone()
            self.assertIsNone(result)

    def tearDown(self):
        # Ensure sequence is dropped if it exists
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP SEQUENCE IF EXISTS {self.sequence_name};")
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
