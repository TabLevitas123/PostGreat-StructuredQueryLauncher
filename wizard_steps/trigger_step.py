
from base_step import BaseStep
from database.trigger_manager import TriggerManager
from tkinter import Label, Entry, Button, OptionMenu, StringVar

class TriggerStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.trigger_manager = TriggerManager()
        self.timing = StringVar(value="BEFORE")
        self.event = StringVar(value="INSERT")

    def init_ui(self):
        Label(self, text="Trigger Name:").pack(pady=5)
        self.trigger_name_entry = Entry(self)
        self.trigger_name_entry.pack(pady=5)

        Label(self, text="Table Name:").pack(pady=5)
        self.table_name_entry = Entry(self)
        self.table_name_entry.pack(pady=5)

        Label(self, text="Timing:").pack(pady=5)
        timing_options = ["BEFORE", "AFTER"]
        OptionMenu(self, self.timing, *timing_options).pack(pady=5)

        Label(self, text="Event:").pack(pady=5)
        event_options = ["INSERT", "UPDATE", "DELETE"]
        OptionMenu(self, self.event, *event_options).pack(pady=5)

        Label(self, text="Function Name:").pack(pady=5)
        self.function_name_entry = Entry(self)
        self.function_name_entry.pack(pady=5)

        Button(self, text="Create Trigger", command=self.create_trigger).pack(pady=10)
        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def create_trigger(self):
        trigger_name = self.trigger_name_entry.get()
        table_name = self.table_name_entry.get()
        timing = self.timing.get()
        event = self.event.get()
        function_name = self.function_name_entry.get()

        if trigger_name and table_name and event and function_name:
            self.trigger_manager.create_trigger(trigger_name, table_name, timing, event, function_name)
        else:
            print("All fields are required for creating a trigger.")

    def validate(self):
        return all([self.trigger_name_entry.get(), self.table_name_entry.get(), self.function_name_entry.get()])

    def go_next(self):
        if self.validate():
            super().go_next()
