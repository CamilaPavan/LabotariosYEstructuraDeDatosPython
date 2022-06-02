"""
Crear una clase de Peliculas:

Cuyo constructutor debe inicializar los atributos nombre, año, genero, nacionalidad, puntuacion
Se deben crear 4 metodos en la clase:
    Presentar la pelicula: La pelicula {nombre} de {genero} del {año} obtuvo una puntuacion de {puntuacion} y fue filmada en {nacionalidad}
    Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
    Cambiar el genero de una pelicula
    Modificar puntuacion de la pelicula (entre 1 y 10)

El programa debe:
*   Tener un menu con 4 opciones:
    1. Crear una pelicula y guardar su nombre en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula

"""

import clase_peliculas as cp
import gestorDePeliculas as gp

gestor = gp.gestorDePeliculas () #para aceder a los metodos de la clase. 

while True:
    condicion=input(
""" ------ MENU PRINCIPAL ------
Por favor ingrese una opcion
        1. crear una pelicula
        2. verificar pelicula
        3. lista de peliculas con el anio de crecion
        4. Presentar pelicula en lista
        5. cambiar el genero de la pelicula
        6. Salir
Numero : """)
    if (condicion=="1"): 
        gestor.crear_pelicula()
    elif (condicion=="2"):
        gestor.verificar_pelicula()
    elif (condicion=="3"):
        gestor.presentar()
    elif (condicion=="4"):
       pass
    elif (condicion=="5"):
       gestor.cambiar_genero()
    
    elif (condicion=="6"):
        print ("Gracias por usar .....")
        break 
    else:
        print("ninguna opcion correcta")