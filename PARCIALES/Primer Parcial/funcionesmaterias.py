#Funciones relacionadas con la lista MATERIAS, primer parcial

lista_materias = ["matematicas" , "fisica" , "quimica"]

#4.Ver lista de materias (Formato: Materias)
def listar_materias():
    global lista_materias
    print ("MATERIAS:")
    for i in lista_materias:
        print (i)

#5. Agregar materias al sistema (verificando que no exista previamente)
def agregar_materias():
    while True:
        materia_nueva = input("ingrese la nueva materia: ")
        if materia_nueva not in lista_materias:
            lista_materias.append(materia_nueva)
            listar_materias()
            break
        else:
            print ("la materia ya se encuentra en el sistema")



