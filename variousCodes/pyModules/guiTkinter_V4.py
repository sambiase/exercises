import tkinter as tk
from tkinter import *


window = tk.Tk()
window.title('TestGui v1')
window.geometry('300x100')
window.resizable(FALSE, FALSE)


def print_name(self):
    name = name_entry.get()
    print(name)


name_label = tk.Label(window, text='Name: ')
name_entry = tk.Entry(window)

btn = tk.Button(text='Submit', bg='orange')
btn.bind("<Button>", print_name)

name_label.pack()
name_entry.pack()
btn.pack()


window.mainloop()



