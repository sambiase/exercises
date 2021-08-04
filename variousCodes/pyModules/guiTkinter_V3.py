import tkinter as tk

root = tk.Tk()
root.geometry('300x200')
root.title('Test Window')


def print_name():
    print(entry_text.get())
    res_window = tk.Tk()
    res_window.geometry('300x200')
    res_window.title('Resultado')

    res_entry = tk.Label(res_window,text=f'{entry_text.get()}')

    res_entry.pack()
    res_window.mainloop()


entry_text = tk.Entry(root,bg='orange')
btn = tk.Button(text='Submit', command=print_name)

entry_text.pack()
btn.pack()
root.mainloop()