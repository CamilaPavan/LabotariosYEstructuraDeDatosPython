#Funciones que corresponden al primer parcial

lista_alumnos = [["camila","federico"],[12,13],["cami@mm","fede@asd" ]]


#1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail)
def listar_usuarios():
    global lista_alumnos
    print ("\tUSUARIO \t EDAD \t MAIL ")
    for i in range(len(lista_alumnos[0])):
        print (f"\t {lista_alumnos[0][i]}  \t {lista_alumnos[1][i]}  \t {lista_alumnos[2][i]}")

# 2. Permitir al usuario del programa agregar un nuevo alumno (Indicando: nombre_usuario - Edad - Mail)

def agregar_alumno():
    global lista_alumnos
    while True: #Cheque que el nombre no este
        nombre_nuevo = input ("ingrese el nombre del nuevo alumno: ")
        if nombre_nuevo not in lista_alumnos[0]:
            lista_alumnos[0].append (nombre_nuevo)
            break
        else:
            print ("el nombre ya se encuentra en la lista")
    while True: #Cheque la edad ingresada
        try:
            edad_nueva = int(input("ingrese la edad del menor: "))
            if edad_nueva >= 10 and edad_nueva <=18:
                lista_alumnos[1].append(edad_nueva)
                break
            else:
                print("edad no valida")
        except:
            print("la edad ingresada no es valida")
    while True: #Chequea el correo
        mail_nuevo = input ("ingrese el correo: ")
        if "@" in mail_nuevo:
            lista_alumnos [2].append (mail_nuevo)
            break
        else:
            print ("correo no valido")
    listar_usuarios ()

#3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
def editar_edad ():
    global lista_alumnos
    while True:
        try:
            edad_nueva = int(input("ingrese la nueva edad: "))
            if edad_nueva >=10 and edad_nueva <=18:
                break
            else:
                print("edad incorrecta")
        except:
            print("Edad incorrecta")
    listar_usuarios()

    while True:
        alumno_a_cambiar = input ("ingrese el nombre del alumano al que desea cambiar la edad: ")
        if alumno_a_cambiar in lista_alumnos[0]:
            lista_alumnos[1][lista_alumnos[0].index (alumno_a_cambiar)] = edad_nueva
            listar_usuarios()
            break
        else:  
            print("no se encuentro el nombre")
            



