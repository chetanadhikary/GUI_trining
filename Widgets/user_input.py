from tkinter import ttk,filedialog,messagebox
import tkinter as tk

from Database_coding.using_class import Student,store_data

class StudentInputFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        padings = {'padx':5,'pady':5}
        #First Name
        ttk.Label(self,text='First Name').grid(column=1, row=1)
        self.fname_entry = ttk.Entry(self, width=30)
        self.fname_entry.grid(column=2, row=1, columnspan=2)
        #Last Name
        ttk.Label(self, text='Last Name').grid(column=1, row=2)
        self.lname_entry = ttk.Entry(self, width=30)
        self.lname_entry.grid(column=2, row=2, columnspan=2)
