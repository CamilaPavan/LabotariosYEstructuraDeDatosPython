
# lee el fichero linea por linea

#todo el documento
try:
    fichero = open("archivo2.txt",'r')
    linea = fichero.readline()
    while  linea != "":
        print(linea, end="") #se pone porque sino hace dos saltos de lineas, xq el doc ya tiene enters 
        linea = fichero.readline()
    fichero.close()
except:
    print("no existe el archivo")

#alguna linea, si necesito una puntual, con el while
try:
    fichero = open("archivo2.txt",'r')
    print(fichero.readline()) #primera linea
    print(fichero.readline()) #segunda
    print(fichero.readline()) #tercera
    fichero.close()
except:
    print("no existe el archivo")

#LEE CARACTER POR CARACTER
try:
    fichero = open("archivo2.txt",'r')
    caracter = fichero.readline(1)
    while caracter != "":
      print(caracter) #,end="") , para que vayan pegados los caracteres 
      caracter = fichero.readline(1)
    fichero.close()
except:
    print("no existe el archivo")