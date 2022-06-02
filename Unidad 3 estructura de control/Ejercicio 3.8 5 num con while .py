"""
El programa debe:

pedir al usuario 5 datos numericos
verificar que sean enteros y sino pedir nuevamente los 5
cuando se tenga los 5 datos el programa debe devolver el promedio
no deben aparecer errores.
"""

print("Este programa calculará el promedio de 5 números")
i = 1
acum = 0
while i<=5:
    try:
        numero=float(input(f"ingrese el {i}°: "))
        i+=1
        acum+=numero
    except:
        print("No es un número válido")
        #i = 1
        #acum = 0  , en caso de que quiera que empeciece de cero el contador cuando pone un numero mal 
promedio = acum/5
print(f"El promedio de los cinco números ingresados es {promedio}")