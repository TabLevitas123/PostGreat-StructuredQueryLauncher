
from connection_manager import ConnectionManager
from constants import ERROR_MESSAGES

class RoleManager:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def create_role(self, role_name, login=False, superuser=False, password=None):
        if not role_name:
            raise ValueError("Role name is required.")

        role_options = "LOGIN" if login else "NOLOGIN"
        role_options += " SUPERUSER" if superuser else " NOSUPERUSER"
        if password:
            role_options += f" PASSWORD '{password}'"

        create_role_query = f"CREATE ROLE {role_name} WITH {role_options};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(create_role_query)
                print(f"Role '{role_name}' created successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def grant_privilege(self, role_name, privilege, table_name):
        grant_query = f"GRANT {privilege} ON {table_name} TO {role_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(grant_query)
                print(f"Granted '{privilege}' privilege on '{table_name}' to role '{role_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def revoke_privilege(self, role_name, privilege, table_name):
        revoke_query = f"REVOKE {privilege} ON {table_name} FROM {role_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(revoke_query)
                print(f"Revoked '{privilege}' privilege on '{table_name}' from role '{role_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def delete_role(self, role_name):
        delete_role_query = f"DROP ROLE IF EXISTS {role_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(delete_role_query)
                print(f"Role '{role_name}' deleted successfully.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
