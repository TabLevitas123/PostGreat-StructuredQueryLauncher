
import xml.etree.ElementTree as ET
import psycopg2
from psycopg2 import sql
from config import Config
from database.connection_manager import ConnectionManager

class XMLIngestor:
    def __init__(self, table_name, xml_file_path, columns, root_tag, row_tag):
        self.table_name = table_name
        self.xml_file_path = xml_file_path
        self.columns = columns
        self.root_tag = root_tag
        self.row_tag = row_tag
        self.conn_manager = ConnectionManager()

    def read_xml_data(self):
        data = []
        tree = ET.parse(self.xml_file_path)
        root = tree.getroot()
        for row in root.findall(f"./{self.row_tag}"):
            row_data = [row.find(col).text if row.find(col) is not None else None for col in self.columns]
            data.append(tuple(row_data))
        return data

    def insert_data(self):
        data = self.read_xml_data()
        with self.conn_manager.get_cursor() as cursor:
            insert_query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values}) ON CONFLICT DO NOTHING").format(
                table=sql.Identifier(self.table_name),
                fields=sql.SQL(', ').join(map(sql.Identifier, self.columns)),
                values=sql.SQL(', ').join(sql.Placeholder() * len(self.columns))
            )
            cursor.executemany(insert_query, data)
            self.conn_manager.connection.commit()
            print(f"Data from {self.xml_file_path} inserted into {self.table_name} successfully.")

if __name__ == "__main__":
    # Example usage
    table_name = "your_table_name"
    xml_file_path = "your_xml_file.xml"
    columns = ["column1", "column2", "column3"]  # Adjust according to table schema
    root_tag = "root"
    row_tag = "row"

    xml_ingestor = XMLIngestor(table_name, xml_file_path, columns, root_tag, row_tag)
    xml_ingestor.insert_data()
