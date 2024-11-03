
import unittest
import os
from data_ingestion.ingest_sql import SQLIngestor
from database.connection_manager import ConnectionManager

class TestSQLIngestor(unittest.TestCase):
    def setUp(self):
        self.table_name = "test_sql_table"
        self.sql_file_path = "test_data.sql"
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Create test SQL file
        with open(self.sql_file_path, mode="w", encoding="utf-8") as file:
            file.write(f"CREATE TABLE IF NOT EXISTS {self.table_name} (id SERIAL PRIMARY KEY, name VARCHAR(100));\n")
            file.write(f"INSERT INTO {self.table_name} (id, name) VALUES (1, 'Test Name');\n")
            file.write(f"INSERT INTO {self.table_name} (id, name) VALUES (2, 'Another Name');\n")

    def test_execute_sql_file(self):
        sql_ingestor = SQLIngestor(self.sql_file_path)
        sql_ingestor.execute_sql_file()

        # Verify data was inserted
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"SELECT * FROM {self.table_name};")
            result = cursor.fetchall()
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0][1], "Test Name")
            self.assertEqual(result[1][1], "Another Name")

    def tearDown(self):
        # Clean up test table and SQL file
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP TABLE IF EXISTS {self.table_name};")
        os.remove(self.sql_file_path)
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
