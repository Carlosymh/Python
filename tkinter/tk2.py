from tkinter import *
import time

root =Tk()
root.title("Posicionar")
root.geometry("400x200")

def saludo():
    print("Hola")


def minimizar():
    root.iconify()

etiqueta = Label(root, text="Saluda desde aqui")
etiqueta.place(x=30, y=50)
etiqueta1 = Label(root, text="Minimiza desde aqui")
etiqueta1.place(x=30, y=100)

boton1 = Button(root, text="Haz click aqui para saludar", command=saludo)
boton1.place(x=200, y=50)
boton2 = Button(root, text="Haz click aqui para Minimizar", command= minimizar)
boton2.place(x=200, y=100)

root.mainloop()