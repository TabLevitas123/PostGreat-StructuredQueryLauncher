
from base_step import BaseStep
from database.table_manager import TableManager
from tkinter import Label, Entry, Button

class TableStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.table_manager = TableManager()
        self.columns = {}

    def init_ui(self):
        Label(self, text="Table Name:").pack(pady=5)
        self.table_name_entry = Entry(self)
        self.table_name_entry.pack(pady=5)

        Label(self, text="Column Name:").pack(pady=5)
        self.column_name_entry = Entry(self)
        self.column_name_entry.pack(pady=5)

        Label(self, text="Column Type:").pack(pady=5)
        self.column_type_entry = Entry(self)
        self.column_type_entry.pack(pady=5)

        Button(self, text="Add Column", command=self.add_column).pack(pady=10)
        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def add_column(self):
        column_name = self.column_name_entry.get()
        column_type = self.column_type_entry.get()
        if column_name and column_type:
            self.columns[column_name] = column_type
            print(f"Added column: {column_name} ({column_type})")
            self.column_name_entry.delete(0, 'end')
            self.column_type_entry.delete(0, 'end')
        else:
            print("Both column name and type are required.")

    def validate(self):
        table_name = self.table_name_entry.get()
        if not table_name:
            print("Table name is required.")
            return False
        if not self.columns:
            print("At least one column is required.")
            return False
        return True

    def go_next(self):
        if self.validate():
            table_name = self.table_name_entry.get()
            self.table_manager.create_table(table_name, self.columns)
            super().go_next()
