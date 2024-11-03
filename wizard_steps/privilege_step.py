
from base_step import BaseStep
from database.privilege_manager import PrivilegeManager
from tkinter import Label, Entry, Button, OptionMenu, StringVar

class PrivilegeStep(BaseStep):
    def __init__(self, parent, next_step_callback, previous_step_callback):
        super().__init__(parent, next_step_callback, previous_step_callback)
        self.privilege_manager = PrivilegeManager()
        self.privilege = StringVar(value="SELECT")

    def init_ui(self):
        Label(self, text="Role Name:").pack(pady=5)
        self.role_name_entry = Entry(self)
        self.role_name_entry.pack(pady=5)

        Label(self, text="Privilege Type:").pack(pady=5)
        privilege_options = ["SELECT", "INSERT", "UPDATE", "DELETE", "USAGE"]
        OptionMenu(self, self.privilege, *privilege_options).pack(pady=5)

        Label(self, text="Object Name (Table/View/Schema):").pack(pady=5)
        self.object_name_entry = Entry(self)
        self.object_name_entry.pack(pady=5)

        Button(self, text="Grant Privilege", command=self.grant_privilege).pack(pady=10)
        Button(self, text="Next", command=self.go_next).pack(pady=10)
        Button(self, text="Previous", command=self.go_previous).pack(pady=5)

    def grant_privilege(self):
        role_name = self.role_name_entry.get()
        privilege = self.privilege.get()
        object_name = self.object_name_entry.get()

        if role_name and object_name:
            self.privilege_manager.grant_privilege(role_name, privilege, object_name)
        else:
            print("Role name and object name are required.")

    def validate(self):
        role_name = self.role_name_entry.get()
        object_name = self.object_name_entry.get()
        if not role_name or not object_name:
            print("Role name and object name are required.")
            return False
        return True

    def go_next(self):
        if self.validate():
            super().go_next()
