class Persona():
    nombre = False

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        print("Has Creado el Objeto Persona con el nombre {} y el apellido {} ".format(nombre, apellido))

    def datos(self):
        self.nombre = True

persona = Persona("Carlos", "Muñoz")