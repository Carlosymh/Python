class Persona():
    nombre = "Carlos"
    apellido = "Muñoz"
    sexo = "Hombre"
    edad = 23

    def hablar(self,mensaje):
        return mensaje

persona = Persona()
persona.nombre
persona.apellido
persona.sexo
persona.edad

print(persona.hablar("Hola soy"),"{} y mi apellido es {} , tengo {} años y soy {}".format(persona.nombre,persona.apellido,persona.edad,persona.sexo))