
from base_step import BaseStep
from database.role_manager import RoleManager
from tkinter import Label, Entry, Button, Checkbutton, IntVar

class RoleStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.role_manager = RoleManager()
        self.login = IntVar()
        self.superuser = IntVar()

    def init_ui(self):
        Label(self, text="Role Name:").pack(pady=5)
        self.role_name_entry = Entry(self)
        self.role_name_entry.pack(pady=5)

        Checkbutton(self, text="Login Enabled", variable=self.login).pack(pady=5)
        Checkbutton(self, text="Superuser Role", variable=self.superuser).pack(pady=5)

        Label(self, text="Password (optional):").pack(pady=5)
        self.password_entry = Entry(self, show="*")
        self.password_entry.pack(pady=5)

        Button(self, text="Create Role", command=self.create_role).pack(pady=10)
        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def create_role(self):
        role_name = self.role_name_entry.get()
        login_enabled = bool(self.login.get())
        superuser_enabled = bool(self.superuser.get())
        password = self.password_entry.get() if self.password_entry.get() else None

        if role_name:
            self.role_manager.create_role(role_name, login_enabled, superuser_enabled, password)
        else:
            print("Role name is required.")

    def validate(self):
        role_name = self.role_name_entry.get()
        if not role_name:
            print("Role name is required.")
            return False
        return True

    def go_next(self):
        if self.validate():
            super().go_next()
