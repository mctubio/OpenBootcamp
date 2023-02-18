import tkinter
from tkinter import ttk

window = tkinter.Tk()
# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)
# (0,2) (1,2) (2,2)
# (0,3) (1,3) (2,3)
# (0,4) (1,4) (2,4)

def reiniciar():
    selection.set(None)



window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=4)

selection = tkinter.StringVar()

rb_01 = ttk.Radiobutton(window, text='Opción A', value=1, variable=selection)
rb_02 = ttk.Radiobutton(window, text='Opción B', value=2, variable=selection)
rb_03 = ttk.Radiobutton(window, text='Opción C', value=3, variable=selection)
rb_04 = ttk.Radiobutton(window, text='Otras', value=4, variable=selection)
rb_01.grid(column=0, row=0, sticky=tkinter.W, padx=10, pady = 10)
rb_02.grid(column=0, row=1, sticky=tkinter.W, padx=10, pady = 10)
rb_03.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady = 10)
rb_04.grid(column=0, row=3, sticky=tkinter.W, padx=10, pady = 10)

boton_reiniciar = tkinter.Button(window, text='REINICIAR', command=reiniciar)
boton_reiniciar.grid(column=2, row=4, sticky=tkinter.E, padx=10, pady = 10)


window.mainloop()
