
import tkinter as tk
from tkinter import messagebox

class ErrorDialog:
    @staticmethod
    def show_error(message, title="Error"):
        messagebox.showerror(title, message)
