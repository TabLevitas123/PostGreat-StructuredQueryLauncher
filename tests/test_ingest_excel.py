
import unittest
import os
import pandas as pd
from data_ingestion.ingest_excel import ExcelIngestor
from database.connection_manager import ConnectionManager

class TestExcelIngestor(unittest.TestCase):
    def setUp(self):
        self.table_name = "test_excel_table"
        self.excel_file_path = "test_data.xlsx"
        self.sheet_name = "Sheet1"
        self.columns = ["id", "name"]
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Create test Excel file
        df = pd.DataFrame({"id": [1, 2], "name": ["Test Name", "Another Name"]})
        df.to_excel(self.excel_file_path, sheet_name=self.sheet_name, index=False)

        # Create test table
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (id SERIAL PRIMARY KEY, name VARCHAR(100));")

    def test_insert_data(self):
        excel_ingestor = ExcelIngestor(self.table_name, self.excel_file_path, self.sheet_name, self.columns)
        excel_ingestor.insert_data()

        # Verify data was inserted
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"SELECT * FROM {self.table_name};")
            result = cursor.fetchall()
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0][1], "Test Name")
            self.assertEqual(result[1][1], "Another Name")

    def tearDown(self):
        # Clean up test table and Excel file
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP TABLE IF EXISTS {self.table_name};")
        os.remove(self.excel_file_path)
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
