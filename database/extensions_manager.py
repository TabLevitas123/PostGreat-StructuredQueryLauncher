
from connection_manager import ConnectionManager
from constants import ERROR_MESSAGES

class ExtensionsManager:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def enable_extension(self, extension_name):
        if not extension_name:
            raise ValueError("Extension name is required.")

        enable_extension_query = f"CREATE EXTENSION IF NOT EXISTS {extension_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(enable_extension_query)
                print(f"Extension '{extension_name}' enabled successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def disable_extension(self, extension_name):
        if not extension_name:
            raise ValueError("Extension name is required.")

        disable_extension_query = f"DROP EXTENSION IF EXISTS {extension_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(disable_extension_query)
                print(f"Extension '{extension_name}' disabled successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
