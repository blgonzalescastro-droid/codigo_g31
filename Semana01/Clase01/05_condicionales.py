edad=10

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

calificacion = 85

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bien")
elif calificacion >= 70:
    print("Bien")
else:
    print("Necesitas mejorar")
    
    
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad >= 18 and not tiene_licencia:
    print("Necesitas una licencia para conducir")
else:
    print("Eres menor de edad, no puedes conducir")
