import os
path = os.path.abspath(os.path.dirname(__file__))

#Escribir lista
try:
    fichero = open(path+"\\archivo_tabla.csv", 'w')
    lista = ["Manzana", "Pera", "Plátano"]
    for linea in lista:
        fichero.write(linea+",")
    fichero.close()
except:
    print("no existe el archivo")



#MATRIZ
try:
    fichero = open(path+"\\archivo_tabla.csv", 'a+')
    lista = [["Manzana", "Pera", "Plátano"],["1","2","3"]]
    for linea in lista:
        for i in linea:
            fichero.write(i+",")
        fichero.write("\n")
    fichero.close()
except:
    print("no existe el archivo")