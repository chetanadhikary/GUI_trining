from tkinter import ttk
import tkinter as tk

from Widgets.user_input import StudentInputFrame
from Widgets.update_record import StudentUpdateFrame


class RootWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, padx=10)
        input_frame = StudentInputFrame(notebook)
        update_frame = StudentUpdateFrame(notebook)
        input_frame.pack(fill='both', expand=True)
        update_frame.pack(fill='both', expand=True)
        notebook.add(input_frame, text='Student Log Entry')
        notebook.add(update_frame, text='Update Student Records')


if __name__ == '__main__':
    root_window = RootWindow()
    root_window.title('Student DataBase')
    root_window.mainloop()
