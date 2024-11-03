
import csv
import psycopg2
from psycopg2 import sql
from config import Config
from database.connection_manager import ConnectionManager

class CSVIngestor:
    def __init__(self, table_name, csv_file_path, columns):
        self.table_name = table_name
        self.csv_file_path = csv_file_path
        self.columns = columns
        self.conn_manager = ConnectionManager()

    def read_csv_data(self):
        data = []
        with open(self.csv_file_path, mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                row_data = [row[col] for col in self.columns]
                data.append(tuple(row_data))
        return data

    def insert_data(self):
        data = self.read_csv_data()
        with self.conn_manager.get_cursor() as cursor:
            insert_query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values}) ON CONFLICT DO NOTHING").format(
                table=sql.Identifier(self.table_name),
                fields=sql.SQL(', ').join(map(sql.Identifier, self.columns)),
                values=sql.SQL(', ').join(sql.Placeholder() * len(self.columns))
            )
            cursor.executemany(insert_query, data)
            self.conn_manager.connection.commit()
            print(f"Data from {self.csv_file_path} inserted into {self.table_name} successfully.")

if __name__ == "__main__":
    # Example usage
    table_name = "your_table_name"
    csv_file_path = "your_csv_file.csv"
    columns = ["column1", "column2", "column3"]  # Adjust according to table schema

    csv_ingestor = CSVIngestor(table_name, csv_file_path, columns)
    csv_ingestor.insert_data()
