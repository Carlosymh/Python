Diccionario= {1 : "Casillas", 15 : "Ramos",3 : "Pique", 5 : "Puyol",11 : "Capdevila", 14 : "Xabi Alonso",16 : "Busquets", 8 : "Xavi Hernandez",18 :"Pedrito", 6 : "Iniesta",7 : "Villa"}

numero= int(input("Ingresa un NUmero de Jugador: "))

if numero in Diccionario:
    print("El Jugador NUmero {} ES".format(numero),Diccionario[numero])
else:
    print("El Numero de jugador {} no Existe en el Diccionario".format(numero))