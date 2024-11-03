
import tkinter as tk

class Navbar:
    def __init__(self, parent, on_next, on_previous):
        self.frame = tk.Frame(parent)
        self.frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.previous_button = tk.Button(self.frame, text="Previous", command=on_previous)
        self.previous_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.next_button = tk.Button(self.frame, text="Next", command=on_next)
        self.next_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def update_buttons(self, is_first_step, is_last_step):
        self.previous_button.config(state=tk.DISABLED if is_first_step else tk.NORMAL)
        self.next_button.config(state=tk.DISABLED if is_last_step else tk.NORMAL)
