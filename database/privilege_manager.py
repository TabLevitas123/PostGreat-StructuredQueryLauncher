
from connection_manager import ConnectionManager
from constants import ERROR_MESSAGES

class PrivilegeManager:
    def __init__(self):
        self.connection_manager = ConnectionManager()

    def grant_privilege(self, role_name, privilege, object_name, object_type="TABLE"):
        grant_query = f"GRANT {privilege} ON {object_type} {object_name} TO {role_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(grant_query)
                print(f"Granted '{privilege}' on '{object_type} {object_name}' to role '{role_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def revoke_privilege(self, role_name, privilege, object_name, object_type="TABLE"):
        revoke_query = f"REVOKE {privilege} ON {object_type} {object_name} FROM {role_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(revoke_query)
                print(f"Revoked '{privilege}' on '{object_type} {object_name}' from role '{role_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def grant_schema_privilege(self, role_name, privilege, schema_name):
        grant_query = f"GRANT {privilege} ON SCHEMA {schema_name} TO {role_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(grant_query)
                print(f"Granted '{privilege}' privilege on schema '{schema_name}' to role '{role_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)

    def revoke_schema_privilege(self, role_name, privilege, schema_name):
        revoke_query = f"REVOKE {privilege} ON SCHEMA {schema_name} FROM {role_name};"

        try:
            with self.connection_manager as cursor:
                cursor.execute(revoke_query)
                print(f"Revoked '{privilege}' privilege on schema '{schema_name}' from role '{role_name}'.")
        except Exception as e:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"], e)
