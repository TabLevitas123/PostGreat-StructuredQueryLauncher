
import unittest
import os
from data_ingestion.ingest_csv import CSVIngestor
from database.connection_manager import ConnectionManager

class TestCSVIngestor(unittest.TestCase):
    def setUp(self):
        self.table_name = "test_csv_table"
        self.csv_file_path = "test_data.csv"
        self.columns = ["id", "name"]
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Create test CSV file
        with open(self.csv_file_path, mode="w", encoding="utf-8") as file:
            file.write("id,name\n1,Test Name\n2,Another Name\n")

        # Create test table
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (id SERIAL PRIMARY KEY, name VARCHAR(100));")

    def test_insert_data(self):
        csv_ingestor = CSVIngestor(self.table_name, self.csv_file_path, self.columns)
        csv_ingestor.insert_data()

        # Verify data was inserted
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"SELECT * FROM {self.table_name};")
            result = cursor.fetchall()
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0][1], "Test Name")
            self.assertEqual(result[1][1], "Another Name")

    def tearDown(self):
        # Clean up test table and CSV file
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP TABLE IF EXISTS {self.table_name};")
        os.remove(self.csv_file_path)
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
