
import tkinter as tk

class Footer:
    def __init__(self, parent, text=""):
        self.frame = tk.Frame(parent)
        self.frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

        self.label = tk.Label(self.frame, text=text, wraplength=500, justify=tk.LEFT)
        self.label.pack(pady=5)

    def update_text(self, text):
        self.label.config(text=text)
