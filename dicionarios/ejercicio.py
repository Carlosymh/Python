Diccionario={"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Ingresa un Pais: ")
letra = pais.capitalize() in Diccionario

if letra:
    print("La capital de {} es:".format(pais),Diccionario[pais.capitalize()])
else:
    pais("El pais {} no se encuentra en el Diccionario".format(pais))