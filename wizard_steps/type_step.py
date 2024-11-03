
from base_step import BaseStep
from database.type_manager import TypeManager
from tkinter import Label, Entry, Button

class TypeStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.type_manager = TypeManager()

    def init_ui(self):
        Label(self, text="Type Name:").pack(pady=5)
        self.type_name_entry = Entry(self)
        self.type_name_entry.pack(pady=5)

        Label(self, text="Values (comma-separated for ENUM):").pack(pady=5)
        self.values_entry = Entry(self)
        self.values_entry.pack(pady=5)

        Button(self, text="Create Type", command=self.create_type).pack(pady=10)
        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def create_type(self):
        type_name = self.type_name_entry.get()
        values = self.values_entry.get().split(",") if self.values_entry.get() else []

        if type_name and values:
            self.type_manager.create_enum_type(type_name, values)
        else:
            print("Type name and values are required for creating ENUM type.")

    def validate(self):
        return bool(self.type_name_entry.get() and self.values_entry.get())

    def go_next(self):
        if self.validate():
            super().go_next()
