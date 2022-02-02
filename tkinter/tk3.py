from tkinter import *

root= Tk()
root.title("Entrada")
root.geometry("350x300")
root.resizable(0,0)

def saludar():
    saludo.set("Hola "+nombre.get()+" "+apellido.get())
    nombre.set(" ")
    apellido.set(" ")
nombre=StringVar()
apellido=StringVar()
saludo = StringVar()


etiqueta1 = Label(root, text="escribe aqui tu nombre: ", bd=4, bg="blue", font=("Curier 10"))
etiqueta1.place(x=10, y=10)
entrada1=Entry(root,textvariable=nombre, bd=5)
entrada1.place(x=170, y=10)

etiqueta2 = Label(root, text="escribe aqui tu apellido: ", bd=4, bg="blue", font=("Curier 10"))
etiqueta2.place(x=10, y=40)
entrada2=Entry(root,textvariable=apellido, bd= 5)
entrada2.place(x=170, y=40)

boton= Button(root, text="Saludar ahora",command=saludar, bd=5, bg="blue")
boton.place(x=10, y=100)

entrada3 = Entry(root, bd=15, font=("Curie 10"), textvariable=saludo,state="disable", bg="blue")
entrada3.place(x=70, y=221)




root.mainloop()