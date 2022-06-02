"""
Crear una clase de Persona:

Cuyo constructutor debe inicializar los atributos nombre, apellido, edad, ciudad_de_recidencia
Se deben crear dos metodos en la clase:
Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad de recidencia}
Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolecente (14 a 22), Joven (22 a 30), mayor(30 a 50), mas mayor(50 a 120)

Menu:
1.CREAR PERSONA
2. SEGUN el nombre indicar edad 

"""
import clases_presentarse as clp
import funciones_main as fn


    
while True:
    opcion =input("""
    ------ menu principal-----
    1. Crear Personas
    2. Verificar rango edad
    3. listar personas
    4. Salir
    opcion: """) 
    if (opcion=="1"): 
        fn.crear_personas()
    elif (opcion=="2"):
        fn.consultar_rango()
    elif (opcion=="3"):
        fn.listar_personas()
    elif (opcion=="4"):
        break
    else:
        print("Opcion incorrecta")




