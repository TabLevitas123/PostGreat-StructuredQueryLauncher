
from connection_manager import ConnectionManager
from constants import DATABASE_ELEMENTS, ERROR_MESSAGES

class SchemaCreator:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def create_schema(self, schema_name, owner=None):
        if not schema_name:
            raise ValueError("Schema name cannot be empty.")

        create_schema_query = f"CREATE SCHEMA {schema_name}"
        if owner:
            create_schema_query += f" AUTHORIZATION {owner};"
        else:
            create_schema_query += ";"

        try:
            with self.connection_manager as cursor:
                cursor.execute(create_schema_query)
                print(f"Schema '{schema_name}' created successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def delete_schema(self, schema_name, cascade=False):
        delete_query = f"DROP SCHEMA {schema_name}"
        delete_query += " CASCADE;" if cascade else ";"

        try:
            with self.connection_manager as cursor:
                cursor.execute(delete_query)
                print(f"Schema '{schema_name}' deleted successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
