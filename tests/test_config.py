
import unittest
import os
from config import Config

class TestConfig(unittest.TestCase):
    def setUp(self):
        # Set up a new config instance for each test
        self.config = Config()

    def test_default_config(self):
        # Test default configuration values
        self.assertEqual(self.config.get("host"), "")
        self.assertEqual(self.config.get("port"), 5432)
        self.assertEqual(self.config.get("user"), "")
        self.assertEqual(self.config.get("database"), "")

    def test_save_and_load_config(self):
        # Modify config and save it
        self.config.set("host", "localhost")
        self.config.set("user", "test_user")
        self.config.save_config()

        # Reload config to ensure it was saved correctly
        loaded_config = Config()
        self.assertEqual(loaded_config.get("host"), "localhost")
        self.assertEqual(loaded_config.get("user"), "test_user")

    def tearDown(self):
        # Clean up by removing config and encryption key files
        if os.path.exists(self.config.CONFIG_FILE):
            os.remove(self.config.CONFIG_FILE)
        if os.path.exists(self.config.ENCRYPTION_KEY_FILE):
            os.remove(self.config.ENCRYPTION_KEY_FILE)

if __name__ == "__main__":
    unittest.main()
