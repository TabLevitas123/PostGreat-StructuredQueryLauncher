
from connection_manager import ConnectionManager
from constants import ERROR_MESSAGES

class ViewManager:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def create_view(self, view_name, query):
        if not view_name or not query:
            raise ValueError("View name and query are required.")

        create_view_query = f"CREATE VIEW {view_name} AS {query};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(create_view_query)
                print(f"View '{view_name}' created successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def create_materialized_view(self, view_name, query, refresh_interval=None):
        if not view_name or not query:
            raise ValueError("View name and query are required.")

        create_view_query = f"CREATE MATERIALIZED VIEW {view_name} AS {query};"
        try:
            with self.connection_manager as cursor:
                cursor.execute(create_view_query)
                print(f"Materialized view '{view_name}' created successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

        if refresh_interval:
            self.set_materialized_view_refresh(view_name, refresh_interval)

    def set_materialized_view_refresh(self, view_name, interval):
        try:
            with self.connection_manager as cursor:
                refresh_query = f"ALTER MATERIALIZED VIEW {view_name} SET (autovacuum_enabled = true, autovacuum_vacuum_threshold = {interval});"
                cursor.execute(refresh_query)
                print(f"Materialized view '{view_name}' set to refresh at interval '{interval}' successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def drop_view(self, view_name, materialized=False):
        view_type = "MATERIALIZED VIEW" if materialized else "VIEW"
        drop_view_query = f"DROP {view_type} IF EXISTS {view_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(drop_view_query)
                print(f"{view_type} '{view_name}' dropped successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
