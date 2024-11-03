
from connection_manager import ConnectionManager
from constants import ERROR_MESSAGES

class IndexManager:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def create_index(self, index_name, table_name, columns, index_type="btree", unique=False):
        if not index_name or not table_name or not columns:
            raise ValueError("Index name, table name, and columns are required.")

        columns_list = ", ".join(columns)
        unique_clause = "UNIQUE" if unique else ""
        create_index_query = f"CREATE {unique_clause} INDEX {index_name} ON {table_name} USING {index_type} ({columns_list});"

        try:
            with self.connection_manager as cursor:
                cursor.execute(create_index_query)
                print(f"Index '{index_name}' created on table '{table_name}' successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def drop_index(self, index_name):
        drop_index_query = f"DROP INDEX IF EXISTS {index_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(drop_index_query)
                print(f"Index '{index_name}' dropped successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
