#Las funciones dan respuesta al ejercicio 5.9 , primer simulacro de parcial 
#Se prueban las dos formas de comentar


Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[10,30,50]]

"""-----------CON KM, INDICAR POSIBLES AUTOS---------------"""
def indentificar_posibles_taxis():
    global Taxis
    while True:
        try:
            recorrido= float(input("ingrese la cantidad de km: "))
            if recorrido > 0:
                break
        except:
            print("ingrese un valor numerico")
    for  i in range(len(Taxis[0])):
        if  recorrido <= Taxis[2][i]:
            print(f"lo puede llevar el: {Taxis[0][i]} ")
        else:
            print(f"el taxi {Taxis[0][i]} no puede llevarlo")



"""----------LISTADO DE AUTOS, CHOFERES Y KM------------------"""
def  listar ():
    global Taxis
    print ( "AUTO - CHOFER - RECORRIDO" )
    for  i  in  range ( len ( Taxis [ 0 ])):
        print ( f" { Taxis [ 0 ][ i ] } - { Taxis [ 1 ][ i ] } - { Taxis [ 2 ][ i ] } " )


# ----------- Modificar nombre chofer segun el nombre del auto -------
def modificar_nombre():
    listar ()
    global Taxis
    while True:
        indicar_auto= input("ingrese el auto a modificar:")
        if indicar_auto in Taxis [0]: 
            Taxis [1][Taxis [0]. index ( indicar_auto )] =  input ( "Nuevo nombre del chofer: " )
            listar()
            return
        else:
            print("no existe ese auto")

     
#Modificar el recorrido segun el nombre del auto.
def modificar_recorrido():
    global Taxis
    listar ()
    while True:
        indicar_auto =input ("ingrese el auto que desea modificar el recorrido: ")
        if indicar_auto in Taxis[0]:
            while True:
                try:
                    kilometros = float(input("ingrese el nuevo recorrido en km: "))
                    break
                except:
                    print ("kilometros incorrectos, intente nuevamente")
            Taxis[2][Taxis[0].index (indicar_auto)] = kilometros
            listar ()
            return
        else:
            print("no existe ese auto")


#Observar informacion de un chofer, verificando su existencia previamente
def info_del_chofer ():
    listar ()
    while True:
        chofer = input ("ingrese el nombre del chofer a verificar: ")
        if chofer in Taxis [1]:
            print (f" El chofer maneja el {Taxis[0][Taxis[1].index(chofer)]} , y hace {Taxis[2][Taxis[1].index(chofer)]} km")
            return

        else:
            print("Nombre incorrecto")    


#Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo
def agregar_nuevo_taxi():
    global Taxis
    while True:
        try:
            nombre_taxi = input ("ingrese el nombre del nuevo taxi: ")
            nombre_chofer = input ("ingrese el nombre del nuevo chofer: ")
            cantidad_km = float(input("ingrese la cantidad de kilometros: "))
            break
        except:
            print("Datos incorrectos")
    Taxis[0].append (nombre_taxi)
    Taxis[1].append (nombre_chofer)
    Taxis [2].append (cantidad_km)    
    listar ()
    


