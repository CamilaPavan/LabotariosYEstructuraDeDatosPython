#pedir al usuario una palabra y encontrar la cantidad de veces que aparece esa palabra en el archivo

"""
pedir al usuario una palabra y encontrar la cantidad de veces que aparece esa palabra en el archivo
"""

import os
#path actual
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°
path_archivo = path+"\\archivo2.txt"
print(path+"\\archivo2.txt")##\\ por caracteres especiales

def imprimir_cantidad_de_palabra ():
    palabra = input ("ingrese la palabra que sea buscar: ")
    try:
        fichero = open(path_archivo,'r')
        texto = fichero.read()
        palabras = texto.split()
        contador = 0
        for i in palabras:
            if i == palabra:
                contador +=1
        print (f"la palabra {palabra} se encuentra {contador} veces")
        fichero.close()
    except:
        print ("el documento no existe")

imprimir_cantidad_de_palabra()
