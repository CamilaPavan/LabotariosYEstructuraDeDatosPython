"""
El programa debe:

Pedir al usuario 3 notas de 3 parciales diferentes
verificar que los ingresados sean correctos
En caso correcto imprimir el promedio
En caso contrario imprimir un error
"""

try:
    nota_1 = float (input('ingrese la nota del primer parcial: '))
    nota_2 = float (input('ingrese la segunda nota: '))
    nota_3= float (input('ingrese la terce nota: '))
    print (f"el promedio de las 3 notas es: {(nota_1 + nota_2 + nota_3)/3}")
except:
    print('Error en las notas')
