class Alumno():
    def  datos(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def Nombre(self):
        print("El nombre del alumno es:",self.nombre)

    def imprimir(self):
        print("NOmbre:",self.nombre)
        print("NOta:",self.nota)

    def resultado(self):
        if self.nota < 5:
            print("Has Reprobado")
        else:
            print("Has Aprobado")

alumno1 = Alumno()
alumno1.datos("Carlos", 8)

alumno2 = Alumno()
alumno2.datos("Michel", 4)

alumno1.resultado()
alumno2.resultado()
