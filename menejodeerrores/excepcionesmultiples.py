while True:
    try:
        num1 = int(input("Ingresa un Numero: "))
        resultado = 100 / num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre cero")


while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es: ",edad)
        break
    except ValueError:
        print("Ingresa un Valor Valido")
        break

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es: ",edad)
        break
    except KeyboardInterrupt():
        print("\nHas Cancelado la Ejecucion")
        break

