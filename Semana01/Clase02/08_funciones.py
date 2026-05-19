

# print(resultado)

def saludar(nombre="Invitado"):
    print(f"Hola, {nombre}!")
    
saludar() # Llamada a la función para ejecutar su código
saludar("Alice") # Llamada a la función con un argumento específico

def mostrar_numeros(*numeros):
    for numero in numeros:
        print(numero)

mostrar_numeros(1, 2, 3, 4, 5) # Llamada a la función con varios argumentos

def mostar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
        
mostar_info(nombre="John", edad=30, ciudad="New York") # Llamada a la función con varios argumentos clave-valor