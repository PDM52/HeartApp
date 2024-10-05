import tkinter as tk
from tkinter import ttk


class Form(ttk.Frame):
    def __init__(self, parent, page_index, label_data, action):
        super().__init__(parent)

        self.page_index = page_index

        frame = ttk.Frame(self, padding="10")
        frame.grid(row=0, column=0, sticky="ew")

        self.entries = {}

        i = 0
        for field in label_data:
            label = ttk.Label(self, text=field)
            label.grid(row=i, column=0, sticky="w")
            if len(label_data[field]) > 0:
                combo_box = ttk.Combobox(self, width=50, values=label_data[field].tolist())
                combo_box.grid(row=i, column=1, sticky="e", padx=200, pady=10)
                self.entries[field] = combo_box
            else:
                entry = ttk.Entry(self, width=53)
                entry.grid(row=i, column=1, sticky="e", padx=200, pady=10)
                self.entries[field] = entry

            i += 1

        submit_button = ttk.Button(self, text="Next", command=action)
        submit_button.grid(row=i+1, column=1, sticky="e", padx=200, pady=10)