class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, que tal {self.nombre}?") 
        

John = Persona("John", 30)
John.saludar() # Output: Hola, que tal John?
print(John.nombre) # Output: John
print(John.edad) # Output: 30

Jane = Persona("Jane", 25)
print(Jane.nombre) # Output: Jane
print(Jane.edad) # Output: 25
Jane.saludar() # Output: Hola, que tal Jane?

class Estudiante(Persona):
    def hablar(self):
        print(f"Hola, soy un estudiante .")
        
Maria = Estudiante("Maria", 20)
print(Maria.nombre) # Output: Maria
Maria.hablar() # Output: Hola, soy un estudiante

class Profesor(Persona):
    def hablar(self):
        print(f"Hola, soy un profesor .")
        
Carlos = Profesor("Carlos", 40)
print(Carlos.nombre) # Output: Carlos
Carlos.hablar() # Output: Hola, soy un profesor

"""Encapsulamiento: Es el concepto de ocultar los detalles internos de una clase y exponer solo lo necesario a través de métodos públicos.
Esto se logra utilizando atributos privados (con doble guion bajo) y métodos públicos para acceder a ellos.
"""

class CuentaBancaria:
    def __init__(self, titular, saldo, clave):
        self.titular = titular
        self.__saldo = saldo
        self.__clave = clave # Atributo privado, no accesible desde fuera de la clase
        
    def __validar_clave(self, clave):
        return clave == self.__clave
        
    def depositar(self, cantidad, clave):
        if self.__validar_clave(clave):
            self.__saldo += cantidad
        else:
            print("Clave incorrecta")
            
    def retirar(self, cantidad, clave):
        if self.__validar_clave(clave):
            if cantidad <= self.__saldo:
                self.__saldo -= cantidad
            else:
                print("Fondos insuficientes")
        else:
            print("Clave incorrecta")
            
    def mostrar_saldo(self):
        print(f"El saldo de la cuenta de {self.titular} es: {self.__saldo}")
        
cuenta = CuentaBancaria("Ana", 1000, "1234")
print(cuenta.titular) # Output: Ana
print(cuenta.__saldo) # Output: 1000
cuenta.mostrar_saldo() # Output: El saldo de la cuenta de Ana es: 1000
cuenta.depositar(500, "1234") # Deposita 500
cuenta.mostrar_saldo() # Output: El saldo de la cuenta de Ana es: 1500
cuenta.retirar(200)
cuenta.mostrar_saldo() # Output: El saldo de la cuenta de Ana es: 1300
cuenta.retirar(2000) # Output: Fondos insuficientes

