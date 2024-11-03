
from base_step import BaseStep
from database.constraint_manager import ConstraintManager
from tkinter import Label, Entry, Button, OptionMenu, StringVar

class ConstraintStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.constraint_manager = ConstraintManager()
        self.constraint_type = StringVar(value="Primary Key")

    def init_ui(self):
        Label(self, text="Table Name:").pack(pady=5)
        self.table_name_entry = Entry(self)
        self.table_name_entry.pack(pady=5)

        Label(self, text="Constraint Type:").pack(pady=5)
        constraint_options = ["Primary Key", "Foreign Key", "Unique", "Check"]
        OptionMenu(self, self.constraint_type, *constraint_options).pack(pady=5)

        Label(self, text="Column Name:").pack(pady=5)
        self.column_name_entry = Entry(self)
        self.column_name_entry.pack(pady=5)

        Label(self, text="Reference Table (for FK):").pack(pady=5)
        self.ref_table_entry = Entry(self)
        self.ref_table_entry.pack(pady=5)

        Label(self, text="Reference Column (for FK):").pack(pady=5)
        self.ref_column_entry = Entry(self)
        self.ref_column_entry.pack(pady=5)

        Label(self, text="Check Condition (for Check):").pack(pady=5)
        self.check_condition_entry = Entry(self)
        self.check_condition_entry.pack(pady=5)

        Button(self, text="Add Constraint", command=self.add_constraint).pack(pady=10)
        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def add_constraint(self):
        table_name = self.table_name_entry.get()
        constraint_type = self.constraint_type.get()
        column_name = self.column_name_entry.get()

        if constraint_type == "Primary Key":
            self.constraint_manager.add_primary_key(table_name, column_name)
        elif constraint_type == "Foreign Key":
            ref_table = self.ref_table_entry.get()
            ref_column = self.ref_column_entry.get()
            self.constraint_manager.add_foreign_key(table_name, column_name, ref_table, ref_column)
        elif constraint_type == "Unique":
            self.constraint_manager.add_unique_constraint(table_name, column_name)
        elif constraint_type == "Check":
            condition = self.check_condition_entry.get()
            self.constraint_manager.add_check_constraint(table_name, f"chk_{column_name}", condition)

    def validate(self):
        table_name = self.table_name_entry.get()
        column_name = self.column_name_entry.get()
        if not table_name or not column_name:
            print("Table name and column name are required.")
            return False
        return True

    def go_next(self):
        if self.validate():
            super().go_next()
