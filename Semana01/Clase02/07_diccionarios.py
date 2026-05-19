usuario = {
    "nombre": "John Doe",
    "edad": 30,
    "email": "john.doe@example.com",
    "es_programador":True,
    "lenguajes": ["Python", "JavaScript", "C++"]
}

print(usuario["nombre"]) # John Doe
print(usuario["edad"]) # 30

"""Modificar elementos del diccionario"""
usuario["edad"] = 31 #  31 es el nuevo valor asociado a la clave "edad"
print(usuario["edad"]) # 31

"""Agregar nuevos elementos al diccionario"""
usuario["pais"] = "Estados Unidos" # pais = "Estados Unidos" es la nueva clave-valor agregada al diccionario
print(usuario["pais"]) # Estados Unidos

"""Eliminar elementos del diccionario"""
del usuario["email"]# Elimina la clave "email" y su valor asociado
usuario.pop("es_programador") # Elimina la clave "es_programador" y devuelve su valor asociado
print(usuario) # Imprime el diccionario actualizado

"""Metodos de los diccionarios"""

print(usuario.keys()) # Imprime todas las claves del diccionario
print(usuario.values()) # Imprime todos los valores del diccionario
print(usuario.items()) # Imprime todos los pares clave-valor del diccionario

for clave, valor in usuario.items():
    print(f"{clave}: {valor}") # Imprime cada clave y su valor asociado en una línea separada