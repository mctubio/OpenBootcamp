import tkinter
from tkinter import ttk

window = tkinter.Tk()

# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)
# (0,2) (1,2) (2,2)
# (0,3) (1,3) (2,3)
# (0,4) (1,4) (2,4)


lista_original = ['cosa 1', 'cosa 2', 'cosa 3', 'todas las cosas']

lista_item = tkinter.StringVar(value=lista_original)

window.title('Ejercicio 10 B')
label = tkinter.Label(window, text='Esto es una lista de cosas', bg='red', fg='yellow')
label.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady = 10)

listbox = tkinter.Listbox(window,  listvariable=lista_item )
listbox.grid(column=1, row=0, sticky=tkinter.N, padx=10, pady = 10)



window.mainloop()