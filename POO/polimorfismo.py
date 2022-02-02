class Animales():
    def __init__(self,nombre,mensaje):
        self.nombre=nombre
        self.mensaje=mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo Hago Guau!")

class Pez(Animales):
    def hablar(self):
        print("Yo No Hablo")

perro = Perro("Firulais", "Guau!")
perro.hablar()

animales = [Perro("Firilais","Guau!"),Pez("Nemo","Nada")]

for i in animales:
    print(i.hablar())