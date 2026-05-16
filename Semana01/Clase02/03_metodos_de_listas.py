animales = ["perro", "gato", "pájaro"]

'append() agrega un elemento al final de la lista'
animales.append("pez")
print(animales)
# Output: ['perro', 'gato', 'pájaro', 'pez']

'insert() agrega un elemento en una posición específica'
animales.insert(1, "conejo")
print(animales)
# Output: ['perro', 'conejo', 'gato', 'pájaro', 'pez']

'extend() agrega los elementos de otra lista al final de la lista actual'
animales.extend(["hamster", "tortuga"])
print(animales)
# Output: ['perro', 'conejo', 'gato', 'pájaro', 'pez', 'hamster', 'tortuga']

'remove() elimina la primera aparición de un elemento específico'
animales.remove("gato")
print(animales)
# Output: ['perro', 'conejo', 'pájaro', 'pez', 'hamster', 'tortuga']

'pop() elimina un elemento en una posición específica y lo devuelve'
animales.pop(2)
print(animales)
# Output: ['perro', 'conejo', 'pez', 'hamster', 'tortuga']

'del elimina un elemento en una posición específica sin devolverlo'
del animales[0]
print(animales)
# Output: ['conejo', 'pez', 'hamster', 'tortuga']

numeros_ordenados = sort (numeros)
print(numeros_ordenados)
# Output: None (sort() no devuelve una nueva lista, sino que ordena la lista original)