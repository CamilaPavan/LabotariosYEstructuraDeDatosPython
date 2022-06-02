"""
El programa va tener una  clase auto con , los siquientes atributos:
Nacionalidad = argentina #GLOBAL
Color
Marca
Modelo
Patente #Unico

el menu principal permite:
    Agregar nuevo auto
    Consultar segun el ano si el auto es:
        - viejo: menos del 2000
        - medio: de 2000 a 2010
        - nuevo : de 2010 a 2020
    listar autos

"""
import funciones_main as fm


while True:
    opcion = input ("""
    ------- MENU PRINCIPAL ------
        1 . Agregar nuevo auto
        2.  Rango por la edad
        3. listar autos
        4. salir
    opcion:  """)
    if opcion == "1":
        fm.crear_auto()
    elif opcion == "2":
        fm.consultar_rango()
    elif opcion == "3":
        fm.listar_autos()
    elif opcion == "4":
        break
    else:
        print ("opcion incorrecta")