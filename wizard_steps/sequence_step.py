
from base_step import BaseStep
from database.sequence_manager import SequenceManager
from tkinter import Label, Entry, Button, Checkbutton, IntVar

class SequenceStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.sequence_manager = SequenceManager()
        self.cycle = IntVar()

    def init_ui(self):
        Label(self, text="Sequence Name:").pack(pady=5)
        self.sequence_name_entry = Entry(self)
        self.sequence_name_entry.pack(pady=5)

        Label(self, text="Start Value:").pack(pady=5)
        self.start_value_entry = Entry(self)
        self.start_value_entry.insert(0, "1")
        self.start_value_entry.pack(pady=5)

        Label(self, text="Increment:").pack(pady=5)
        self.increment_entry = Entry(self)
        self.increment_entry.insert(0, "1")
        self.increment_entry.pack(pady=5)

        Label(self, text="Minimum Value (optional):").pack(pady=5)
        self.min_value_entry = Entry(self)
        self.min_value_entry.pack(pady=5)

        Label(self, text="Maximum Value (optional):").pack(pady=5)
        self.max_value_entry = Entry(self)
        self.max_value_entry.pack(pady=5)

        Checkbutton(self, text="Cycle", variable=self.cycle).pack(pady=5)

        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def validate(self):
        sequence_name = self.sequence_name_entry.get()
        if not sequence_name:
            print("Sequence name is required.")
            return False
        return True

    def go_next(self):
        if self.validate():
            sequence_name = self.sequence_name_entry.get()
            start = int(self.start_value_entry.get())
            increment = int(self.increment_entry.get())
            min_value = int(self.min_value_entry.get()) if self.min_value_entry.get() else None
            max_value = int(self.max_value_entry.get()) if self.max_value_entry.get() else None
            cycle = bool(self.cycle.get())

            self.sequence_manager.create_sequence(sequence_name, start, increment, min_value, max_value, cycle)
            super().go_next()
