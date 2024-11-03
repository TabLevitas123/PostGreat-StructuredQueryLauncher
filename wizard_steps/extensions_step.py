
from base_step import BaseStep
from database.extensions_manager import ExtensionsManager
from tkinter import Label, Entry, Button

class ExtensionsStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.extensions_manager = ExtensionsManager()

    def init_ui(self):
        Label(self, text="Extension Name:").pack(pady=5)
        self.extension_name_entry = Entry(self)
        self.extension_name_entry.pack(pady=5)

        Button(self, text="Enable Extension", command=self.enable_extension).pack(pady=10)
        Button(self, text="Disable Extension", command=self.disable_extension).pack(pady=10)
        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def enable_extension(self):
        extension_name = self.extension_name_entry.get()
        if extension_name:
            self.extensions_manager.enable_extension(extension_name)
        else:
            print("Extension name is required to enable it.")

    def disable_extension(self):
        extension_name = self.extension_name_entry.get()
        if extension_name:
            self.extensions_manager.disable_extension(extension_name)
        else:
            print("Extension name is required to disable it.")

    def validate(self):
        return bool(self.extension_name_entry.get())

    def go_next(self):
        if self.validate():
            super().go_next()
