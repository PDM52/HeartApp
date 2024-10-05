import pickle
import tkinter as tk

import pandas as pd
import pycaret
from tkinter import ttk
from form import Form


class App:
    def show_frame(self, frame):
        frame.tkraise()
        self.shown_frames.append(frame)

    def submit_form(self):
        data = {}
        for frame in self.frames:
            for field in frame.entries:
                try:
                    data[field] = [frame.entries[field].getint()]
                except:
                    data[field] = [frame.entries[field].get()]

        with open('GradientBoostingClassifier.pkl', 'rb') as file:
            model = pickle.load(file)
        processed_data = pd.DataFrame(data).drop(columns=['HadHeartAttack'])
        prediction = model.predict(processed_data)
        print(prediction)

    def show_next_page(self):
        for frame in self.frames:
            if frame not in self.shown_frames:
                self.show_frame(frame)
                return
            else:
                frame.grid_forget()

    def __init__(self, root, data):
        self.root = root
        self.container = ttk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.frames = []
        self.shown_frames = []

        data_quarter = len(data) // 4

        items = list(data.items())

        sliced_data = [dict(items[:data_quarter]), dict(items[data_quarter:2 * data_quarter]),
                       dict(items[2 * data_quarter:3 * data_quarter]), dict(items[3 * data_quarter:])]

        i = 1
        for data_slice in sliced_data:
            f = Form
            if i < len(sliced_data):
                action = self.show_next_page
            else:
                action = self.submit_form
            frame = f(self.container, i, data_slice, action)
            self.frames.append(frame)
            frame.grid(row=0, column=0, sticky="nsew")
            i += 1

        self.show_frame(self.frames[0])


with open('dictionary.pkl', 'rb') as pickle_file:
    label_data = pickle.load(pickle_file)

root = tk.Tk()
app = App(root, label_data)

root.mainloop()
