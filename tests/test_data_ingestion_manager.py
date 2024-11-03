
import unittest
from unittest.mock import patch
from data_ingestion_manager import DataIngestionManager

class TestDataIngestionManager(unittest.TestCase):
    def setUp(self):
        self.manager = DataIngestionManager()

    @patch("data_ingestion.ingest_csv.CSVIngestor.insert_data")
    def test_ingest_csv(self, mock_insert):
        self.manager.ingest_csv("test_table", "test.csv", ["id", "name"])
        mock_insert.assert_called_once()

    @patch("data_ingestion.ingest_json.JSONIngestor.insert_data")
    def test_ingest_json(self, mock_insert):
        self.manager.ingest_json("test_table", "test.json", ["id", "name"])
        mock_insert.assert_called_once()

    @patch("data_ingestion.ingest_xml.XMLIngestor.insert_data")
    def test_ingest_xml(self, mock_insert):
        self.manager.ingest_xml("test_table", "test.xml", ["id", "name"], "root", "row")
        mock_insert.assert_called_once()

    @patch("data_ingestion.ingest_sql.SQLIngestor.execute_sql_file")
    def test_ingest_sql(self, mock_execute):
        self.manager.ingest_sql("test.sql")
        mock_execute.assert_called_once()

    @patch("data_ingestion.ingest_excel.ExcelIngestor.insert_data")
    def test_ingest_excel(self, mock_insert):
        self.manager.ingest_excel("test_table", "test.xlsx", "Sheet1", ["id", "name"])
        mock_insert.assert_called_once()

if __name__ == "__main__":
    unittest.main()
