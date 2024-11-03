
from connection_manager import ConnectionManager
from constants import ERROR_MESSAGES

class TriggerManager:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def create_trigger(self, trigger_name, table_name, timing, event, function_name):
        if not trigger_name or not table_name or not event or not function_name:
            raise ValueError("Trigger name, table name, event, and function name are required.")

        create_trigger_query = (f"CREATE TRIGGER {trigger_name} "
                                f"{timing} {event} ON {table_name} "
                                f"FOR EACH ROW EXECUTE FUNCTION {function_name}();")

        try:
            with self.connection_manager as cursor:
                cursor.execute(create_trigger_query)
                print(f"Trigger '{trigger_name}' created on table '{table_name}' for {event} event.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def drop_trigger(self, trigger_name, table_name):
        drop_trigger_query = f"DROP TRIGGER IF EXISTS {trigger_name} ON {table_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(drop_trigger_query)
                print(f"Trigger '{trigger_name}' dropped from table '{table_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def enable_trigger(self, trigger_name, table_name):
        enable_trigger_query = f"ALTER TABLE {table_name} ENABLE TRIGGER {trigger_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(enable_trigger_query)
                print(f"Trigger '{trigger_name}' enabled on table '{table_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def disable_trigger(self, trigger_name, table_name):
        disable_trigger_query = f"ALTER TABLE {table_name} DISABLE TRIGGER {trigger_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(disable_trigger_query)
                print(f"Trigger '{trigger_name}' disabled on table '{table_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
