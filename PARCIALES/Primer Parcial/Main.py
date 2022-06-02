"""
ENUNCIADO: "Programa de Gestión de alumnos y Materias"

Introduccion: 
    El siguiente programa consiste en un software de gestion de alumnos y gestion de materias
    de una institucion educativa.
    El programa debe permitir agregar y quitar alumnos al sistema junto con su informacion personal: 
    Nombre, Edad y mail.
    El programa debe permitir agregar Materias al sistema.

Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail)
    2. Permitir al usuario del programa agregar un nuevo alumno (Indicando: nombre_usuario - Edad - Mail)
       Verificando: Que el nombre_usuario no exista previamente, la edad entre 10 y 18 años y que el mail cuente con un @.
       (Ayuda: metodo in de list sirve tambien para strings)
    3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
    4. Ver lista de materias (Formato: Materias)
    5. Agregar materias al sistema (verificando que no exista previamente)
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
"""
import funcionesalumnos as fa
import funcionesmaterias as fm



while True:
    condicion=input(
""" ------ MENU PRINCIPAL ------
Por favor ingrese una opcion
        1. ver lista de alumnos
        2. agregar nuevo alumno
        3. editar edad de alumno existente
        4. Ver lista materias
        5. Agregar materias al sistema
        6. Salir
Numero : """)
    if (condicion=="1"): 
        fa.listar_usuarios()
    elif (condicion=="2"):
        fa.agregar_alumno()
    elif (condicion=="3"):
        fa.editar_edad()
    elif (condicion=="4"):
       fm.listar_materias()
    elif (condicion == "5"):
        fm.agregar_materias()
    elif (condicion == "6"):
        print ("Gracias por usar el sistema ")
        break
    else:
        print("ninguna opcion correcta, intente nuevamente")

