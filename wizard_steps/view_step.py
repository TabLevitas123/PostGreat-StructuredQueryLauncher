
from base_step import BaseStep
from database.view_manager import ViewManager
from tkinter import Label, Entry, Button, Checkbutton, IntVar

class ViewStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.view_manager = ViewManager()
        self.is_materialized = IntVar()

    def init_ui(self):
        Label(self, text="View Name:").pack(pady=5)
        self.view_name_entry = Entry(self)
        self.view_name_entry.pack(pady=5)

        Label(self, text="SQL Query:").pack(pady=5)
        self.query_entry = Entry(self, width=50)
        self.query_entry.pack(pady=5)

        Checkbutton(self, text="Materialized View", variable=self.is_materialized).pack(pady=5)

        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def validate(self):
        view_name = self.view_name_entry.get()
        query = self.query_entry.get()

        if not view_name:
            print("View name is required.")
            return False
        if not query:
            print("SQL query is required.")
            return False
        return True

    def go_next(self):
        if self.validate():
            view_name = self.view_name_entry.get()
            query = self.query_entry.get()
            materialized = bool(self.is_materialized.get())

            if materialized:
                self.view_manager.create_materialized_view(view_name, query)
            else:
                self.view_manager.create_view(view_name, query)

            super().go_next()
