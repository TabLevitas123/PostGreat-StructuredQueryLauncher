
import tkinter as tk

class FormBuilder:
    def __init__(self, parent):
        self.parent = parent
        self.entries = {}

    def add_text_field(self, label_text, field_name, default_value=""):
        label = tk.Label(self.parent, text=label_text)
        label.pack(pady=5)
        entry = tk.Entry(self.parent)
        entry.insert(0, default_value)
        entry.pack(pady=5)
        self.entries[field_name] = entry

    def get_field_value(self, field_name):
        entry = self.entries.get(field_name)
        if entry:
            return entry.get()
        return None

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
