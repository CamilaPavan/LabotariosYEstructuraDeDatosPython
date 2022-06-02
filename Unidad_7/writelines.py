import os
path = os.path.abspath(os.path.dirname(__file__))


#Todo junto, en la misma linea
try:
    fichero = open(path+"\\archivo_escribir.txt", 'w')
    lista = ["Manzana", "Pera", "Plátano"]
    fichero.writelines(lista)
    fichero.close()
except:
    print("no existe el archivo")


#Uno abajo del otro los elementos de una lista:
try:
    fichero = open(path+"\\archivo_escribir.txt", 'w+')#a+
    lista = ["Manzana\n", "Pera\n", "Plátano\n"] #se separa con el \n para el salto. 
    fichero.writelines(lista)
    fichero.close()
except:
    print("no existe el archivo")

#crear un csv
try:
    fichero = open(path+"\\test_w.csv", 'w+')
    lista = ["Manzana,", "Pera,", "Plátano,"] #se separa con comas
    fichero.writelines(lista)
    fichero.close()
except:
    print("no existe el archivo")

