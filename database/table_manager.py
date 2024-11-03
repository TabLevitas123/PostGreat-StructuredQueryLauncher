
from connection_manager import ConnectionManager
from constants import ERROR_MESSAGES

class TableManager:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def create_table(self, table_name, columns):
        if not table_name:
            raise ValueError("Table name cannot be empty.")
        if not columns or not isinstance(columns, dict):
            raise ValueError("Columns must be a dictionary with column names and types.")

        columns_definition = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
        create_table_query = f"CREATE TABLE {table_name} ({columns_definition});"

        try:
            with self.connection_manager as cursor:
                cursor.execute(create_table_query)
                print(f"Table '{table_name}' created successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def add_column(self, table_name, column_name, data_type):
        add_column_query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(add_column_query)
                print(f"Column '{column_name}' added to table '{table_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def drop_table(self, table_name, cascade=False):
        drop_query = f"DROP TABLE {table_name}"
        drop_query += " CASCADE;" if cascade else ";"

        try:
            with self.connection_manager as cursor:
                cursor.execute(drop_query)
                print(f"Table '{table_name}' deleted successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
