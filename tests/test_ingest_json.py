
import unittest
import os
import json
from data_ingestion.ingest_json import JSONIngestor
from database.connection_manager import ConnectionManager

class TestJSONIngestor(unittest.TestCase):
    def setUp(self):
        self.table_name = "test_json_table"
        self.json_file_path = "test_data.json"
        self.columns = ["id", "name"]
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Create test JSON file
        test_data = [{"id": 1, "name": "Test Name"}, {"id": 2, "name": "Another Name"}]
        with open(self.json_file_path, mode="w", encoding="utf-8") as file:
            json.dump(test_data, file)

        # Create test table
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (id SERIAL PRIMARY KEY, name VARCHAR(100));")

    def test_insert_data(self):
        json_ingestor = JSONIngestor(self.table_name, self.json_file_path, self.columns)
        json_ingestor.insert_data()

        # Verify data was inserted
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"SELECT * FROM {self.table_name};")
            result = cursor.fetchall()
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0][1], "Test Name")
            self.assertEqual(result[1][1], "Another Name")

    def tearDown(self):
        # Clean up test table and JSON file
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP TABLE IF EXISTS {self.table_name};")
        os.remove(self.json_file_path)
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
