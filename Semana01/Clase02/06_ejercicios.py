"""Crea una aplicación que busque la palabra ingresada"""

palabra = [ "rojo", "azul", "verde", "amarillo", "negro"]

busqueda = input("Ingrese la palabra a buscar: ")

se_encontro = False
for mensaje in palabra:
    if mensaje == busqueda:
        print(f"Palabra encontrada: {mensaje}")
        se_encontro = True
        break
if se_encontro == False:
    print("Palabra no encontrada")