from tkinter import *
import time

root=Tk()
root.title("Mi primer ventana")
root.geometry("500x300")

boton1 = Button(root, text="Minimizar", command=root.iconify, bg="Red")
boton1.pack(side=LEFT)
def imprimir():
     label1 = Label(root,text="Imprimiendo......")
     label1.pack()


boton2 = Button(root, text="Imprimirt", command=imprimir, bg="blue")
boton2.pack(side=RIGHT)










root.mainloop()
