
import unittest
from database.privilege_manager import PrivilegeManager
from database.role_manager import RoleManager
from database.connection_manager import ConnectionManager

class TestPrivilegeManager(unittest.TestCase):
    def setUp(self):
        # Initialize the PrivilegeManager, RoleManager, and ConnectionManager
        self.privilege_manager = PrivilegeManager()
        self.role_manager = RoleManager()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Define a test role and test table
        self.role_name = "test_role"
        self.role_manager.create_role(self.role_name, login=True)

    def test_grant_table_privilege(self):
        table_name = "pg_catalog.pg_class"  # Using a system table for testing
        self.privilege_manager.grant_privilege(self.role_name, "SELECT", table_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT has_table_privilege(%s, %s, 'SELECT');", (self.role_name, table_name))
            result = cursor.fetchone()
            self.assertTrue(result[0])

    def test_revoke_table_privilege(self):
        table_name = "pg_catalog.pg_class"
        self.privilege_manager.grant_privilege(self.role_name, "SELECT", table_name)
        self.privilege_manager.revoke_privilege(self.role_name, "SELECT", table_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT has_table_privilege(%s, %s, 'SELECT');", (self.role_name, table_name))
            result = cursor.fetchone()
            self.assertFalse(result[0])

    def tearDown(self):
        # Drop the test role and close connection
        self.role_manager.delete_role(self.role_name)
        self.conn_manager.close_connection()

if __name__ == "__main__":
    unittest.main()
