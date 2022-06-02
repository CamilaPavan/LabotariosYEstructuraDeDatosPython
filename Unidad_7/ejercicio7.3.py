"""Ejercicio 7.3
Crear una funcion para leer el un archivo.txt.

Crear funciones para:

Contar la cantidad de letrar que tiene el archivo (letras no espacios ni puntos)
Contar la cantidad de palabras que tiene el archivo"""

def contador_palabras ():
    try:
        fichero = open("ejercicio1.txt", 'r')
        texto = fichero.read()
        palabras = texto.split()
        contador = 0
        for i in palabras:
            contador +=1
        print (f"el doc tiene {contador} palabras")
        fichero.close()
    except:
        print ("el documento no existe")


def contar_letras():
    try:
        fichero = open("ejercicio1.txt","r")
        cant_letras = 0
        while True:
            letra = fichero.readline(1)
            if (letra == ""): #indico que llegue al fin 
                break
            elif(letra != "." and letra != " "):
                cant_letras+=1
            
        fichero.close()
        print(f"La cant de letras son {cant_letras}")
        
    except:
        print("no existe el archivo")

contar_letras()