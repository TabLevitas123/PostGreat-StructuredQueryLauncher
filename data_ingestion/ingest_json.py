
import json
import psycopg2
from psycopg2 import sql
from config import Config
from database.connection_manager import ConnectionManager

class JSONIngestor:
    def __init__(self, table_name, json_file_path, columns):
        self.table_name = table_name
        self.json_file_path = json_file_path
        self.columns = columns
        self.conn_manager = ConnectionManager()

    def read_json_data(self):
        data = []
        with open(self.json_file_path, mode="r", encoding="utf-8") as file:
            json_data = json.load(file)
            for item in json_data:
                row_data = [item.get(col) for col in self.columns]
                data.append(tuple(row_data))
        return data

    def insert_data(self):
        data = self.read_json_data()
        with self.conn_manager.get_cursor() as cursor:
            insert_query = sql.SQL("INSERT INTO {table} ({fields}) VALUES ({values}) ON CONFLICT DO NOTHING").format(
                table=sql.Identifier(self.table_name),
                fields=sql.SQL(', ').join(map(sql.Identifier, self.columns)),
                values=sql.SQL(', ').join(sql.Placeholder() * len(self.columns))
            )
            cursor.executemany(insert_query, data)
            self.conn_manager.connection.commit()
            print(f"Data from {self.json_file_path} inserted into {self.table_name} successfully.")

if __name__ == "__main__":
    # Example usage
    table_name = "your_table_name"
    json_file_path = "your_json_file.json"
    columns = ["column1", "column2", "column3"]  # Adjust according to table schema

    json_ingestor = JSONIngestor(table_name, json_file_path, columns)
    json_ingestor.insert_data()
