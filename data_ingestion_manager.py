
from data_ingestion.ingest_csv import CSVIngestor
from data_ingestion.ingest_json import JSONIngestor
from data_ingestion.ingest_xml import XMLIngestor
from data_ingestion.ingest_sql import SQLIngestor
from data_ingestion.ingest_excel import ExcelIngestor

class DataIngestionManager:
    def __init__(self):
        pass

    def ingest_csv(self, table_name, csv_file_path, columns):
        ingestor = CSVIngestor(table_name, csv_file_path, columns)
        ingestor.insert_data()

    def ingest_json(self, table_name, json_file_path, columns):
        ingestor = JSONIngestor(table_name, json_file_path, columns)
        ingestor.insert_data()

    def ingest_xml(self, table_name, xml_file_path, columns, root_tag, row_tag):
        ingestor = XMLIngestor(table_name, xml_file_path, columns, root_tag, row_tag)
        ingestor.insert_data()

    def ingest_sql(self, sql_file_path):
        ingestor = SQLIngestor(sql_file_path)
        ingestor.execute_sql_file()

    def ingest_excel(self, table_name, excel_file_path, sheet_name, columns):
        ingestor = ExcelIngestor(table_name, excel_file_path, sheet_name, columns)
        ingestor.insert_data()

if __name__ == "__main__":
    # Example CLI integration or usage could be added here.
    pass
