import os
#path actual
path = os.path.abspath(os.path.dirname(__file__))
print("c:/Users/Camila/Documents/Lab Algoritmo y estructutura de Datos/Unidad_7\archivo.txt"+"\\archivo.txt")##\\ por caracteres especiales



try:
    fichero = open ("archivo.txt",'r')#fichero = open(path+"\\archivo.txt", 'r')#
    print(fichero.read()) #Ver todo el contenido
    fichero.close()
except:
    print("no existe el archivo")



