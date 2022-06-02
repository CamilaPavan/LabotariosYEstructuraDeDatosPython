import os
"""#path actual
path = os.path.abspath(os.path.dirname(__file__))
print(path+"\\archivo.txt")##\\ por caracteres especiales"""


import os
#path actual
path = os.path.abspath(os.path.dirname(__file__))
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°
path_archivo = path+"\\archivo.txt" #NOMBRE DEL ARCHIVO
print(path+"\\archivo.txt")##\\ por caracteres especiales



try:
    fichero = open (f"{path_archivo},'r'")#fichero = open(path+"\\archivo.txt", 'r')#
    print(fichero.read()) #Ver todo el contenido
    fichero.close()
except:
    print("no existe el archivo")