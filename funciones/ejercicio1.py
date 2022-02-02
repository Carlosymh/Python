lista = []
num = 0

def pedir():
    i=0
    while i < 5:
        num = int(input("Ingrese un numero: "))
        lista.append(num)
        i += 1

def numeros():
    lista.sort()
    pares = []
    impar = []
    for i in lista: 
        if i%2 == 0:
            pares.append(i)
        else:
            impar.append(i)
    print(pares)
    print(impar)

pedir()
numeros()

