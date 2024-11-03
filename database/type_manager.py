
from connection_manager import ConnectionManager
from constants import ERROR_MESSAGES

class TypeManager:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def create_enum_type(self, type_name, values):
        if not type_name or not values or not isinstance(values, list):
            raise ValueError("Type name and a list of values are required for ENUM type.")

        formatted_values = ", ".join([f"'{value}'" for value in values])
        create_type_query = f"CREATE TYPE {type_name} AS ENUM ({formatted_values});"

        try:
            with self.connection_manager as cursor:
                cursor.execute(create_type_query)
                print(f"ENUM type '{type_name}' created with values {values}.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def drop_type(self, type_name):
        drop_type_query = f"DROP TYPE IF EXISTS {type_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(drop_type_query)
                print(f"Type '{type_name}' dropped successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
