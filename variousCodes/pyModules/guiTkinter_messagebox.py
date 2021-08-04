import tkinter as tk
from tkinter import messagebox,FALSE

window = tk.Tk()
window.title('TestGui v1')
window.geometry('300x100')
window.resizable(FALSE, FALSE)

tk.messagebox.showerror(title='Erro',message="Teste de Erro")
tk.messagebox.askokcancel(title='Ask to Cancel', message='Want to Cancel?')
tk.messagebox.askretrycancel(title='Try Again?',message='Try again?')

try:
    a + 3
except Exception:
    raise ValueError(tk.messagebox.showerror(title='Erro',message='Erro de Input'))


window.mainloop()



