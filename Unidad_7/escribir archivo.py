import os
path = os.path.abspath(os.path.dirname(__file__))

try:
    fichero = open(path+"\\archivo_nuevo.txt", 'a+') #a+ para que se sume, y no pise lo que estaba
    lista = ["Manzana", "Pera", "Platano"]
    for linea in lista:
        fichero.write(linea + "\n") #si no le pongo \n, escribe una cosa al lado de la otra 
        #fichero.write(linea)
    fichero.close()
except:
    print("no existe el archivo")

#si saco el a+, cada vez que ejecuto, piso la info que tenia