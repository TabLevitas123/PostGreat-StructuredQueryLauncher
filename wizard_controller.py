
import tkinter as tk
from wizard_steps import (
    SchemaStep, TableStep, IndexStep, ViewStep, SequenceStep, ConstraintStep, RoleStep,
    PrivilegeStep, TriggerStep, TypeStep, ExtensionsStep
)
from constants import ERROR_MESSAGES

class WizardController:
    def __init__(self, root, config):
        self.root = root
        self.config = config
        self.steps = [
            SchemaStep, TableStep, IndexStep, ViewStep, SequenceStep, ConstraintStep,
            RoleStep, PrivilegeStep, TriggerStep, TypeStep, ExtensionsStep
        ]
        self.current_step_index = 0
        self.current_step_instance = None
        self.initialize_navigation()

    def initialize_navigation(self):
        self.load_step(self.current_step_index)

    def load_step(self, index):
        if self.current_step_instance:
            self.current_step_instance.pack_forget()
        step_class = self.steps[index]
        self.current_step_instance = step_class(self.root, self.next_step, self.previous_step)
        self.current_step_instance.pack(expand=True, fill="both")

    def next_step(self):
        try:
            if self.current_step_index < len(self.steps) - 1:
                self.current_step_index += 1
                self.load_step(self.current_step_index)
            else:
                print("End of the wizard.")
        except Exception as e:
            print(ERROR_MESSAGES["NAVIGATION_ERROR"], e)

    def previous_step(self):
        try:
            if self.current_step_index > 0:
                self.current_step_index -= 1
                self.load_step(self.current_step_index)
        except Exception as e:
            print(ERROR_MESSAGES["NAVIGATION_ERROR"], e)
