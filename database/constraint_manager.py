
from connection_manager import ConnectionManager
from constants import ERROR_MESSAGES

class ConstraintManager:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def add_primary_key(self, table_name, column_name):
        add_pk_query = f"ALTER TABLE {table_name} ADD PRIMARY KEY ({column_name});"

        try:
            with self.connection_manager as cursor:
                cursor.execute(add_pk_query)
                print(f"Primary key added to column '{column_name}' in table '{table_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def add_foreign_key(self, table_name, column_name, ref_table, ref_column):
        add_fk_query = f"ALTER TABLE {table_name} ADD CONSTRAINT fk_{column_name}_{ref_table} "                        f"FOREIGN KEY ({column_name}) REFERENCES {ref_table} ({ref_column});"

        try:
            with self.connection_manager as cursor:
                cursor.execute(add_fk_query)
                print(f"Foreign key on '{column_name}' referencing '{ref_table}({ref_column})' added to table '{table_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def add_unique_constraint(self, table_name, column_name):
        add_unique_query = f"ALTER TABLE {table_name} ADD CONSTRAINT unique_{column_name} UNIQUE ({column_name});"

        try:
            with self.connection_manager as cursor:
                cursor.execute(add_unique_query)
                print(f"Unique constraint added to column '{column_name}' in table '{table_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def add_check_constraint(self, table_name, constraint_name, condition):
        add_check_query = f"ALTER TABLE {table_name} ADD CONSTRAINT {constraint_name} CHECK ({condition});"

        try:
            with self.connection_manager as cursor:
                cursor.execute(add_check_query)
                print(f"Check constraint '{constraint_name}' with condition '{condition}' added to table '{table_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def drop_constraint(self, table_name, constraint_name):
        drop_query = f"ALTER TABLE {table_name} DROP CONSTRAINT {constraint_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(drop_query)
                print(f"Constraint '{constraint_name}' dropped from table '{table_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
