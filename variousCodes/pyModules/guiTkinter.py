import tkinter as tk

window = tk.Tk()
window.title('MarginTrading Calculator v1')
window.geometry('700x600')
window.configure(bg='#38B6FF')             #cor de fundo da window criada


# Cria um Label Widget - Usado para mostrar texto ou imagens
label = tk.Label(text='Nome', fg='black', bg='red', width=10, height=1)
label.pack()        #mostrar a label na janela criada



# Cria um Entry Widget - coletar input do usuario
entry = tk.Entry(fg='black', bg='white', width=20)
entry.pack()
name = entry.get()
print(name)


# Cria um Text Widget
text_box = tk.Text()
text_box.pack()
print(text_box.get('1.4'))


# Cria um Button Widget
btn = tk.Button(text='Click', fg='black', bg='orange', width=20, height=5)
btn.place(x=490,y=510,width=200,height=80)


# mostra a janela na tela
window.mainloop()
