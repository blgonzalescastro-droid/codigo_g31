"""Crea una calculadora de opraciones aritméticas básicas (suma, resta, multiplicación y división) que solicite al usuario dos números y la operación que desea realizar. El programa debe mostrar el resultado de la operación seleccionada."""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación que desea realizar (suma, resta, multiplicación, división): ")

if operacion == "suma":
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == "resta":
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "multiplicación":
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "división":
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
else:
    print("Operación no válida. Por favor, ingrese una operación válida.")