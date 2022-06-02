"""
Crear una funcion que debe: (usar diccionario)

Crear un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
Pida al usuario el dato a agregar (key) y el valor
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

diccionario = {}

def diccionario_por_usuario():
    while True:
        condicion = input("""Desea agregar informacion al diccionario?
                        1. SI
                        2. NO
                        """)
        if condicion == "1":
            dato= input ("escriba la KEY del dato a ingresar ")
            if dato in diccionario:
                print ("dicha KEY ya se encuentra en el diccionario, prube con otra")
            else:
                informacion = input (f"que desea guardar en {dato}?: ")
                diccionario.update({dato:informacion})
                print (diccionario)
        elif condicion == "2" :
            print (f"Gracias, su diccionario quedo con la siguiente informacion {diccionario}")
            break
        else:
            print("no ingreso una opcion correcta")

def imprimir_diccionario(nombre,diccionario):
  print(f"--------{nombre}--------")
  print(f"--key \t   Valor--")
  for i in diccionario:
    print(f"  {i}\t{diccionario.get(i)}")

diccionario_por_usuario ()
nombre = "diccionario de cami"
imprimir_diccionario(nombre,diccionario)

#--------------------------------------------

personas={}
def agregar_informacion():
  while True:
    key = input("Ingrese la informacion que registrara o salir (para abandonar el programa): ")
    if key =="salir":
      break
    if key in personas:
      print("Ya existe el valor, ingrese uno diferente!!")
    else:
      valor = input(f"Por favor ingrese el valor de {key}: ")
      personas.setdefault(key,valor) #ingresar los dos valores 
      print(personas)

def imprimir_diccionario(nombre,diccionario):
  print(f"--------{nombre}--------")
  print(f"--key\tValor--")
  for i in diccionario:
    print(f"  {i}\t{diccionario.get(i)}")

def imprimir_diccionario2(nombre,diccionario):
  print(f"--------{nombre}--------")
  print(f"--key\tValor--")
  for i,j in diccionario.items(): #i trae los key (tupla) j trae los valores (tupla)
    print(f"  {i}\t{j}")
