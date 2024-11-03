
import unittest
import os
import xml.etree.ElementTree as ET
from data_ingestion.ingest_xml import XMLIngestor
from database.connection_manager import ConnectionManager

class TestXMLIngestor(unittest.TestCase):
    def setUp(self):
        self.table_name = "test_xml_table"
        self.xml_file_path = "test_data.xml"
        self.columns = ["id", "name"]
        self.root_tag = "root"
        self.row_tag = "row"
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Create test XML file
        root = ET.Element(self.root_tag)
        row1 = ET.SubElement(root, self.row_tag)
        ET.SubElement(row1, "id").text = "1"
        ET.SubElement(row1, "name").text = "Test Name"
        row2 = ET.SubElement(root, self.row_tag)
        ET.SubElement(row2, "id").text = "2"
        ET.SubElement(row2, "name").text = "Another Name"
        tree = ET.ElementTree(root)
        tree.write(self.xml_file_path)

        # Create test table
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (id SERIAL PRIMARY KEY, name VARCHAR(100));")

    def test_insert_data(self):
        xml_ingestor = XMLIngestor(self.table_name, self.xml_file_path, self.columns, self.root_tag, self.row_tag)
        xml_ingestor.insert_data()

        # Verify data was inserted
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"SELECT * FROM {self.table_name};")
            result = cursor.fetchall()
            self.assertEqual(len(result), 2)
            self.assertEqual(result[0][1], "Test Name")
            self.assertEqual(result[1][1], "Another Name")

    def tearDown(self):
        # Clean up test table and XML file
        with self.conn_manager.get_cursor() as cursor:
            cursor.execute(f"DROP TABLE IF EXISTS {self.table_name};")
        os.remove(self.xml_file_path)
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
