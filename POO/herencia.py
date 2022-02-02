class Animales():
    def __init__(self,descripcion, especie, hablar):
        self.descripcion = descripcion
        self.especie = especie
        self.hablar=hablar

    def habla(self):
        print("Yo Hago:",self.hablar)
    
    def describir(self):
        print("Soy de la Especie:",self.especie)
class Perro(Animales):
    pass

class Abeja(Animales):
      def sonido(self,sonido):
          self.sonido = sonido
          print(self.sonido)




perro = Perro("Perro","Mamifero","Guau!")
perro.habla()
perro.describir()

abeja = Abeja("Aabeja", "Insecto", "Brrr!")
abeja.sonido("Brr!")
abeja.habla()
abeja.describir()
