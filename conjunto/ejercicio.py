Meses = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

Mes = int(input("Ingrese un numero de mes: "))

if Mes in Meses:
    if Mes == 1:
        print( "El mes 1 es Enero")
    elif Mes == 2:
        print( "El mes 2 es Febrero")
    elif Mes == 3:
        print( "El mes 3 es Marzo")
    elif Mes == 4:
        print( "El mes 4 es Abril")
    elif Mes == 5:
        print( "El mes 5 es Mayo")
    elif Mes == 6:
        print( "El mes 6 es Junio")
    elif Mes == 7:
        print( "El mes 7 es Julio")
    elif Mes == 8:
        print( "El mes 8 es Agusto")
    elif Mes == 9:
        print( "El mes 9 es Septiembre")
    elif Mes == 10:
        print( "El mes 10 es Octubre")
    elif Mes == 11:
        print( "El mes 11 es Nomviembre")
    elif Mes == 12:
        print( "El mes 12 es Diciembre")
else:
    print("El Numero de Mes {} no Existe".format(Mes))