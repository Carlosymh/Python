from tkinter import *
import time

root=Tk()
root.title("Hamburguesas")
root.config(bd=20,bg="orange")

def orden():
    lista=""
    if(queso.get()):
        lista+= "Con Queso "
    else:
     lista+="Sin Queso "

    if (lechuga.get()):
        lista+="y Con Lechuga"
    else:
        lista+="y Sin Lechuga"
    imprimir.config(text=lista)

    




queso=IntVar()
lechuga=IntVar()

imagen = PhotoImage(file="python/gifhamb.gif")
Label(root, image=imagen).pack(side=LEFT)

frame=Frame(root)
frame.pack(side=RIGHT)
frame.config(bg="orange")

Label(frame, text="¿Como quieres tu Hamburguesa?",bg="orange", font="Curriel 15").pack(anchor="w")
Checkbutton(frame, text="Con Queso", variable=queso,onvalue=1, offvalue=0,bg="orange",font="Curiel 10",command=orden).pack(anchor="w")
Checkbutton(frame, text="Con lechuga", variable=lechuga,onvalue=1, offvalue=0,bg="orange",font="Curiel 10",command=orden).pack(anchor="w")

imprimir=Label(frame, bg="orange")
imprimir.pack()
imprimir.config(font="Curriel 15")


root.mainloop()