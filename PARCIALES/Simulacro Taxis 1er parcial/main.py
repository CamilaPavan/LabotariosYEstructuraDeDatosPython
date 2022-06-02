'''
##**Ejercicio 5.9 (Empresa de Taxis)**
El programa debe:
*   Simular una empresa de taxis que cuente con tres Autos con sus respectivos cheferes

    *  Cada auto cuenta con un chofer y no hace recorridos mayores a lo q se le indica
*   Contar con 6 funciones disponibles en el menu:
    1. Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes
    2. Modificar nombre chofer segun el nombre del auto.
        auto_1 -> "federico"
    3. Modificar el recorrido segun el nombre del auto.
        auto_1 -> 60
    4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo -> ULTIMO
    5. Observar una lista de autos choferes y recorrido maximo con el siguiente formato:
    6. Observar informacion de un chofer, verificando su existencia previamente

    
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
import funciones as fn

while True:
    condicion=input(
""" ------ MENU PRINCIPAL ------
Por favor ingrese una opcion
        1. Con el recorrido, saber que chofer hace el viaje
        2. Modificar nombre chofer
        3. Modificar recorrido 
        4. Agregar nuevo auto a la empresa
        5. Observar toda la informacion
        6. Observar info de un chofer
        7. Salir
Numero : """)
    if (condicion=="1"): 
        fn.indentificar_posibles_taxis()
    elif (condicion=="2"):
        fn.modificar_nombre()
    elif (condicion=="3"):
        fn.modificar_recorrido()
    elif (condicion=="4"):
       fn.agregar_nuevo_taxi()
    elif (condicion == "5"):
        fn.listar()
    elif (condicion == "6"):
        fn.info_del_chofer()
    elif (condicion=="7"):
        print ("Gracias por usar el sistema ")
        break 
    else:
        print("ninguna opcion correcta, intente nuevamente")