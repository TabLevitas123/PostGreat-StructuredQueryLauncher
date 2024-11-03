
import unittest
from database.role_manager import RoleManager
from database.connection_manager import ConnectionManager

class TestRoleManager(unittest.TestCase):
    def setUp(self):
        # Initialize the RoleManager and ConnectionManager instances
        self.role_manager = RoleManager()
        self.conn_manager = ConnectionManager()
        self.conn_manager.connect()

        # Define a test role
        self.role_name = "test_role"

    def test_create_role(self):
        self.role_manager.create_role(self.role_name, login=True, superuser=False, password="test_pass")

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT rolname FROM pg_roles WHERE rolname = %s", (self.role_name,))
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], self.role_name)

    def test_grant_privilege(self):
        table_name = "pg_catalog.pg_class"  # Using a system table for testing
        self.role_manager.create_role(self.role_name, login=True)
        self.role_manager.grant_privilege(self.role_name, "SELECT", table_name)

        with self.conn_manager.get_cursor() as cursor:
            cursor.execute("SELECT has_table_privilege(%s, %s, 'SELECT');", (self.role_name, table_name))
            result = cursor.fetchone()
            self.assertTrue(result[0])

    def test_revoke_privilege(self):
        table_name = "pg_catalog.pg_class"
        self.role_manager.create_role(self.role_name, login=True)
        self.role_manager.grant_privilege(self.role_name, "SELECT", table_name)
        self.role_manager.revoke_privilege(self.role_name, "SELECT", table_name)

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
