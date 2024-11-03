
from base_step import BaseStep
from database.index_manager import IndexManager
from tkinter import Label, Entry, Button, Checkbutton, IntVar

class IndexStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.index_manager = IndexManager()
        self.is_unique = IntVar()

    def init_ui(self):
        Label(self, text="Index Name:").pack(pady=5)
        self.index_name_entry = Entry(self)
        self.index_name_entry.pack(pady=5)

        Label(self, text="Table Name:").pack(pady=5)
        self.table_name_entry = Entry(self)
        self.table_name_entry.pack(pady=5)

        Label(self, text="Columns (comma-separated):").pack(pady=5)
        self.columns_entry = Entry(self)
        self.columns_entry.pack(pady=5)

        Label(self, text="Index Type:").pack(pady=5)
        self.index_type_entry = Entry(self)
        self.index_type_entry.insert(0, "btree")  # Default to btree
        self.index_type_entry.pack(pady=5)

        Checkbutton(self, text="Unique Index", variable=self.is_unique).pack(pady=5)

        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def validate(self):
        index_name = self.index_name_entry.get()
        table_name = self.table_name_entry.get()
        columns = self.columns_entry.get()

        if not index_name:
            print("Index name is required.")
            return False
        if not table_name:
            print("Table name is required.")
            return False
        if not columns:
            print("At least one column is required.")
            return False
        return True

    def go_next(self):
        if self.validate():
            index_name = self.index_name_entry.get()
            table_name = self.table_name_entry.get()
            columns = self.columns_entry.get().split(",")
            index_type = self.index_type_entry.get()
            unique = bool(self.is_unique.get())

            self.index_manager.create_index(index_name, table_name, columns, index_type, unique)
            super().go_next()
