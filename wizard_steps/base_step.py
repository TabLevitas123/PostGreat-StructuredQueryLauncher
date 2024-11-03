
import tkinter as tk
from constants import ERROR_MESSAGES

class BaseStep(tk.Frame):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent)
        self.next_step_callback = next_step_callback
        self.previous_step_callback = previous_step_callback
        self.init_ui()

    def init_ui(self):
        # Placeholder UI setup for each step, will be overridden by subclasses
        pass

    def validate(self):
        # Basic validation method, intended to be overridden by subclasses
        return True

    def go_next(self):
        if self.validate():
            self.next_step_callback()
        else:
            print(ERROR_MESSAGES["VALIDATION_FAILURE"])

    def go_previous(self):
        self.previous_step_callback()
