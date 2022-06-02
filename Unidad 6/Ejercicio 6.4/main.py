"""

Ejercicio 6.4
Crear una clase padre Vehiculos:

Constructor debe incluir los atributos (patente,marca,año,origen)
Crear metodos para esta clase de:
Presentarse (patente,marca,año,origen)
Indicar tipos de vehiculo(Clases heredadas)
Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, obtener_velocidad, setear_velocidad
Crear 3 clases que hereden de la clase padre Vehiculos, con un atributo en particular para cada una

Particular
PickUp
Deportivo
Crear clase GestorAutos que cuente con las siguientes funciones para un menu


Crear auto, indicando tipo de auto y guardar en una lista
Listar autos (presentandolos), indicando tipo de Vehiculo.
Cambiar velocidad de un Vehiculo
Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)

"""

import Vehiculos as vh
import GestorAutos as ga

gestor = ga.GestorAuto()

while True:
    condicion=input(
""" ------ MENU PRINCIPAL ------
Por favor ingrese una opcion
        1. Crear auto
        2. Presentar auto
        3. cambiar velocidad
        4. calcular tiempo con km
        5. Salir
Numero : """)
    if (condicion=="1"): 
        gestor.crear_auto()
    elif (condicion=="2"):
        gestor.presentar ()
    elif (condicion=="3"):
        gestor.cambiar_velocidad()
    elif (condicion=="4"):
       gestor.calcular_tiempo()
    elif (condicion=="5"):
        print ("Gracias por usar .....")
        break 
    else:
        print("ninguna opcion correcta")


