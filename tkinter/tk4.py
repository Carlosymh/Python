from tkinter import *
import time

root=Tk()
root.title("Radiobuttons")
root.geometry("400x300")
root.config(bg="silver")
root.resizable(0,0)

def operacion():
    num= int(numero.get())
    numero.set("")
    if opcion.get()==1:
        total= num*5
    elif opcion.get()==2:
        total= num*10
    elif opcion.get()==3:
        total= num*20
    elif opcion.get()==4:
        total= num*30
    elif opcion.get()==5:
        total= num*40
    else:
        total= num*num
    
    print(f"El total de la operacion es :{str(total)}")

opcion=StringVar()
numero=StringVar()

etiqueta1 = Label(root, text="Escriba su Numero",bg="silver",bd=5)
etiqueta1.place(x=20, y=20)

entrada1= Entry(root,bd=7,font="Helvetica 12",textvariable=numero)
entrada1.place(x=150, y=20)

etiqueta2= Label(root, text="Elija la cantidad: ",bg="silver",bd=5)
etiqueta2.place(x=20, y=50)

x5=Radiobutton(root, text="x5", value=1,bg="silver",bd=5,textvariable=opcion)
x5.place(x=20, y=80)

x10=Radiobutton(root, text="x10", value=2,bg="silver",bd=5,textvariable=opcion)
x10.place(x=70, y=80)

x20=Radiobutton(root, text="x20", value=3,bg="silver",bd=5,textvariable=opcion)
x20.place(x=120, y=80)

x30=Radiobutton(root, text="x30", value=4,bg="silver",bd=5,textvariable=opcion)
x30.place(x=20, y=110)

x40=Radiobutton(root, text="x40", value=5,bg="silver",bd=5,textvariable=opcion)
x40.place(x=70, y=110)

boton1 = Button(root, text="Realizar operacion",bg="silver",bd=5, command=operacion)
boton1.place(x=20, y=140)













root.mainloop()