
from base_step import BaseStep
from database.schema_creator import SchemaCreator
from tkinter import Label, Entry, Button

class SchemaStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.schema_creator = SchemaCreator()

    def init_ui(self):
        Label(self, text="Schema Name:").pack(pady=5)
        self.schema_name_entry = Entry(self)
        self.schema_name_entry.pack(pady=5)

        Label(self, text="Owner (optional):").pack(pady=5)
        self.owner_entry = Entry(self)
        self.owner_entry.pack(pady=5)

        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def validate(self):
        schema_name = self.schema_name_entry.get()
        if not schema_name:
            print("Schema name is required.")
            return False
        return True

    def go_next(self):
        if self.validate():
            schema_name = self.schema_name_entry.get()
            owner = self.owner_entry.get() if self.owner_entry.get() else None
            self.schema_creator.create_schema(schema_name, owner)
            super().go_next()
