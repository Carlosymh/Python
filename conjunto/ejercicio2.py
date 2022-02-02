alfabeto = ( "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z")
letra = int(input("Ingresa un Numero de letra: "))
if letra < len(alfabeto)  and letra >= 0:
    print("La letra numero {} es ".format(letra),alfabeto[letra])
else:
    print("La letra numero {} no existe".format(letra))