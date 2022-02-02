class Persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        print("El Objeto {} {} ha sido creado".format(self.nombre,self.apellido))

    def __str__(self):
        return("El Objeto tiene el NOmbre {} y El Apellido {}".format(self.nombre,self.apellido))


    def __del__(self):
        print("El Objeto {} {} ha sido destruido".format(self.nombre,self.apellido))

persona = Persona("Carlos", "Muñoz")
print(str(persona))