def num():
    numero1= int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el Segundo Numero: "))
    if numero1 > numero2:
        return 1
    elif numero1 < numero2:
        return -1
    else:
        return 0

print(num())