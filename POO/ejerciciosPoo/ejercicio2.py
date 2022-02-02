class calculadora():
    def __init__(self):
        self.valor1=int(input("Ingrese el Primer Valor: "))
        self.valor2=int(input("Ingrese el Segundo Valor: "))

    def suma(self):
        self.suma = self.valor1 + self.valor2
        print("La Suma es de ",self.suma)

    def resta(self):
        self.resta = self.valor1 - self.valor2
        print5("La resta es de ",self.resta)

    def multiplicacion(self):
        self.multiplicacion = self.valor1 + self.valor2
        print("La multiplicacion es de ",self.multiplicacion)

    def divicion(self):
        self.divicion = self.valor1 + self.valor2
        print("La divicion es de ",self.divicion)

calcular = calculadora()
calcular.suma()
calcular.resta()
calcular.multiplicacion()
calcular.divicion()