#Crear una funcion para leer el un archivo.txt hasta encontrar un punto.

def imprimir_hasta_punto_while():
    try:
        fichero = open("ejercicio1.txt", 'r')
        while True:
            caracter = fichero.readline(1)
            print(caracter,end="")
            if(caracter=="."):
                break
        fichero.close()
    except:
        print("no existe el archivo")


def imprimir_hasta_punto_for():
    try:
        fichero = open("ejercicio1.txt", 'r')
        for c in fichero.readline():
            print(c,end="")
            if(c=="."):
                break
        fichero.close()
    except:
        print("no existe el archivo")
imprimir_hasta_punto_for()