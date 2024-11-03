
import pandas as pd
import psycopg2
from psycopg2 import sql
from config import Config
from database.connection_manager import ConnectionManager

class ExcelIngestor:
    def __init__(self, table_name, excel_file_path, sheet_name, columns):
        self.table_name = table_name
        self.excel_file_path = excel_file_path
        self.sheet_name = sheet_name
        self.columns = columns
        self.conn_manager = ConnectionManager()

    def read_excel_data(self):
        df = pd.read_excel(self.excel_file_path, sheet_name=self.sheet_name)
        data = df[self.columns].dropna().values.tolist()
        return [tuple(row) for row in data]

    def insert_data(self):
        data = self.read_excel_data()
        with self.conn_manager.get_cursor() as cursor:
            insert_query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values}) ON CONFLICT DO NOTHING").format(
                table=sql.Identifier(self.table_name),
                fields=sql.SQL(', ').join(map(sql.Identifier, self.columns)),
                values=sql.SQL(', ').join(sql.Placeholder() * len(self.columns))
            )
            cursor.executemany(insert_query, data)
            self.conn_manager.connection.commit()
            print(f"Data from {self.excel_file_path} inserted into {self.table_name} successfully.")

if __name__ == "__main__":
    # Example usage
    table_name = "your_table_name"
    excel_file_path = "your_excel_file.xlsx"
    sheet_name = "Sheet1"
    columns = ["column1", "column2", "column3"]  # Adjust according to table schema

    excel_ingestor = ExcelIngestor(table_name, excel_file_path, sheet_name, columns)
    excel_ingestor.insert_data()
