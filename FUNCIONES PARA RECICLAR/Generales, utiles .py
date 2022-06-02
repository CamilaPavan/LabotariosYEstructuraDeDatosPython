#for i in "federico":
#  print (i, end=",") #me imprime todo en el mismo reglon, separdo por coma. 

#para poner la primera letra en mayuscula, en el input
#moneda = input("Ingrese que tipo de moneda desea saber el simbolo: ").capitalize() 

#Pasar de minutos a horas
def minutos_a_hora(minutos):
    horas_finales = 0
    while  minutos > 60:
        minutos = minutos - 60
        horas_finales+=1

    #print(f"los {minutos_iniciales} son {horas_finales} hs:{minutos} min")
    return horas_finales,minutos

#Pedir una palabra
"""
while True:
    palabra= input("Ingrese una palabra: ")
    if not palabra.isalpha():
        print("la palabra no es correcta")
    else:
        break
"""

#FUNCION PARA PEDIR NUMEROS
def pedir_numeros():
  while True: #Lo pongo aca para no usar "try" y "except" en todas las funciones 
    try:
      num1 = float(input("1° numero: "))
      num2 = float(input("2° numero: "))
      break
    except:
      print("argumentos incorrectos")

  return num1,num2 #Permite retornar mas de un argumento, Directamente separados con comas.

#Usuario con 3 oportunidades
def usuario_y_contrasena ():
    for i in range (3):
        usuario = input ("ingrese su usario: ")
        contra = input ("ingrese su contrana: ")
        if usuario == "user" and contra == "1234":
            return True
        else:
            print (f"usurio y contrasenia incorrecta, le quedan {2-i} oportunidades")
    return False

#Imprimir una matriz dinamica, pero con la misma cantidad de Filas y columnas
def  imprimir_matriz2(matriz):
  print (f"-------------- PRODUCTOS --------------")
  print (f"C \t PRODUCTO \t Pr $ \t Stock") #El \t hace un tab en el print
  for  i  in range (len(matriz)- 1 ):
    if i != 0:
      print("") #para que no imprima el espacio
    for  j in range(len(matriz)):
      print (f"{ matriz [ j ] [ i ] } " , end = '\t' ) #\t hace tabulacion y da como cuadro 
  print ("")

#imprimir una matriz FACIL 
def  listar ():
    print ( "AUTO - CHOFER - RECORRIDO" )
    for  i  in  range ( len ( Taxis [ 0 ])): #Aca puedo poner cualquier lista, porque todas tienen la misma longitud
        print ( f" { Taxis [ 0 ][ i ] } - { Taxis [ 1 ][ i ] } - { Taxis [ 2 ][ i ] } " )

#imprimir una matriz, mas facil, pero estatica
def imprimir_matriz(matriz):
    print ("cod  - produc -  $ - stck")
    for i in range(len(matriz)-1): #pongo menos 1 porque sino empieza en 1 y da error
        print(f"{matriz[0][i]} - {matriz[1][i]} - {matriz[2][i]} - {matriz[3][i]}")

#Imprimir un diccionario lindo
def imprimir_diccionario2(nombre,diccionario):
  print(f"--------{nombre}--------")
  print(f"--key\tValor--")
  for i,j in diccionario.items(): #i trae los key (tupla) j trae los valores (tupla)
    print(f"  {i}\t{j}")

#Crear UNICO EN CLASS - IMPORTANTEEEEEEEEEE 
def chequear_que_sea_unico():
  lista_peliculas = [] #NO VA, TIENE QUE ESTAR FUERA DE LA FUNCION. 
    flag_agregar = True
    pelicula_nueva = input("ingrese el nombre de la pelicula: ") 
    for Pelicula in lista_peliculas: #la lista que tengo guardada
        if pelicula_nueva == Pelicula.nombre: #llamo class con el dato unico, en este caso "nombre de la peli"
            print ("Esa pelicula ya se encuentra en la lista")
            flag_agregar = False
            break
    if flag_agregar==True :
        break

#Tipo de clase:
def tipo_vehiculo(self):
    print("Soy un Animal del tipo", type(self).__name__)


#CREAR FICHERO, con palabra que pedimos:
#+ importar path para fichero
import os
path = os.path.abspath(os.path.dirname(__file__))
path_archivo = path+"\\archivo.txt"
def escribir_en_archivo(palabra):
    try:
        fichero = open(path_archivo,'a')
        fichero.write(palabra+"\n")
        fichero.close()
    except:
        print("Error!")

def pedir_palabras():

    while True:
        palabra = input("Ingrese una palabra: (exit->para salir) ")
        if(palabra =="exit"):
            break
        else:
            escribir_en_archivo(palabra)

 #CREAR ARCHIVO CON NOMBRE QUE LE PEDIMOS AL USUARIO
def crear_archivo():
    nombre = input("Ingrese el nombre del archivo: ")
    global path_archivo
    path_archivo = path+ f"\\{nombre}.txt"
    try:
        fichero = open(path_archivo, 'w')
        #fichero.read , no hace falta porque lo estamos creando no mas
        fichero.close()
    except:
        print("ERROR."