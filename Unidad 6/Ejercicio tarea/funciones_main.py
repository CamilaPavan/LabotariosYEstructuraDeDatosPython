"""
El programa va tener una  clase auto con , los siquientes atributos:
Nacionalidad = argentina #GLOBAL
Color
Marca
Modelo
Patente #Unico
"""


import clases_auto as ca

#def __init__(self, color1, marca1, anio1, patente1):

lista_autos = []

def crear_auto():
    color = input ("ingrese el color del nuevo auto: ")
    marca = input ("ingrese la marca del auto: ")

    while True: #chequea que el anio sea valido
        try:
            anio =int(input("ingrese el anio: "))
            if anio >1800:
                break
        except:
            print ("dato incorrecto")

    while True: #pide patente, DATO UNICO
        patente = input ("Inngrese la patente del auto: ")
        flag_agregar = True
        for auto in lista_autos:
            if patente == auto.patente:
                flag_agregar = False
                break
        if flag_agregar == True:
            break
    
    instancia = patente
    instancia = ca.autos ( color, marca, anio,patente)
    lista_autos.append(instancia)



def listar_autos():
    for autos in lista_autos:
        autos.presentarse()


def consultar_rango():
    print("------ Lista de autos------")
    for auto in lista_autos:
        print(f"{auto.marca}\t{auto.color}\t{auto.anio}\t{auto.patente}\t")
    while True: #pide patente
        patente_consultar = input("ingrese la patente a consultar: ")
        for auto in lista_autos:
            if patente_consultar == auto.patente:
                auto.rango_edad()
                return
        else:
            print ("error")
