
import unittest
import tkinter as tk
from main import DatabaseCreationWizard

class TestMain(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = DatabaseCreationWizard(self.root)

    def test_initialization(self):
        self.assertIsNotNone(self.app.controller)
        self.assertIsInstance(self.app.controller, object)

    def test_navigation(self):
        # Test that the wizard can navigate forward
        self.app.controller.next_step()
        self.assertEqual(self.app.controller.current_step_index, 1)

        # Test that the wizard can navigate backward
        self.app.controller.previous_step()
        self.assertEqual(self.app.controller.current_step_index, 0)

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
