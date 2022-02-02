from tkinter import *
#Configuracion de raiz
root=Tk()
 
menuBar=Menu(root)
root.config(menu=menuBar)

archivoMenu = Menu(menuBar,tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=root.quit)


editMenu= Menu(menuBar,tearoff=0)


editMenu.add_command(label="Cortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")

ayudaMenu =Menu(menuBar,tearoff=0)

ayudaMenu.add_command(label="Ayuda")
ayudaMenu.add_separator()

menuBar.add_cascade(label="Archivo",menu=archivoMenu)
menuBar.add_cascade(label="Editar",menu=editMenu)
menuBar.add_cascade(label="Ayuda",menu=ayudaMenu)


root.mainloop()