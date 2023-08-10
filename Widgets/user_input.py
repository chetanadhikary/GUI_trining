from tkinter import ttk,filedialog,messagebox
import tkinter as tk

from Database_coding.using_class import Student,store_data,display_data

class StudentInputFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        padings = {'padx':5,'pady':5}
        #First Name
        ttk.Label(self,text='First Name').grid(column=1, row=1, **padings)
        self.fname_entry = ttk.Entry(self, width=30)
        self.fname_entry.grid(column=2, row=1, columnspan=2)
        #Last Name
        ttk.Label(self, text='Last Name').grid(column=1, row=2,**padings)
        self.lname_entry = ttk.Entry(self, width=30)
        self.lname_entry.grid(column=2, row=2, columnspan=2)
        #Stream Name
        ttk.Label(self, text='Stream Name').grid(column=1, row=3,**padings)
        self.stream_name_entry = ttk.Entry(self, width=30)
        self.stream_name_entry.grid(column=2, row=3, columnspan=2)
        #Store Button
        ttk.Button(self,text='Save',command=self.save_record).grid(column=2,row=4,**padings)
        #Cancel Button
        ttk.Button(self,text='Clear',command=self.clear_record).grid(column=3,row=4,**padings)

    def save_record(self):
        fname = self.fname_entry.get()
        lname = self.lname_entry.get()
        stream = self.stream_name_entry.get()
        stud_obj = Student(fname,lname,stream)
        store_data(stud_obj)
        display_data()

    def clear_record(self):
        self.fname_entry.delete(0,'end')
        self.lname_entry.delete(0,'end')
        self.stream_name_entry.delete(0,'end' )
