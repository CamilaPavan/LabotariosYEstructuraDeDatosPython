'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: EXAMEN FINAL MARZO 2022
 APELLIDO Y NOMBRE: CAMILA PAVAN DESTRU
 DNI: 40.751.923
 CARRERA: Analista de sistemas de computacion
 AÑO: 2022
 Se debe subir en la tarea del classroom, COMPRIMIR EN CARPETA [Apellido,Nombre Examen final marzo 2022]
 ************************************************************
 Ítems a evaluar:
 1. Contenidos de la materia
 2. Requerimientos y comprensión de consignas
 3. Estructura (modularización), legibilidad y comentarios del código.
 4. Compilacion del codigo.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de gestion de local de reparacion de PCs"

Introducción: 
    El siguiente programa consiste en un software que simule una programa para gestionar las computadoras y los tecnicos en un local de reparacion de PCs.
    El programa debe permitir agregar nuevas computadoras (a arreglar) al sistema, como tambien asignarle un tecnico (un tecnico puede arreglar mas de una PC al mismo tiempo).

Requerimientos:
El programa debe:
 *  Contar con una Clase Computadora con los atributos (numero_pc (int - único), descripcion_problema (string), tecnico (string))
 *  Contar con una Clase Hija Notebook que use el constructor de la clase padre
        
 *  Se deben crear los siguientes métodos para la clase padre Computadora (que heredará la clase hija):
        1. mostrar_información: Que indique el numero_pc, tipo de clase (se puede usar funcion get_tipo_clase), descripcion_problema y tecnico asignado.
        2. set_descripcion_problema y get_descripcion_problema
        3. set_tecnico y get_tecnico
        4. get_tipo_clase

 *  Se debe crear una clase GestorComputadoras que cuente con las siguientes funciones para un menu:
    1.  Crear instancias de una Computadora (o notebook) y guárdalos en una lista de computadoras_a_arreglar. 
        1.1) Se debe verificar que tipo de instancia de Computadora a crear y los parámetros (2 clases (Computadora y Notebook)). 
             -> numero_pc: Debe ser único (debe ser un int, y no puede estar repetido)
             -> descripcion_problema: Verificar que el string no sea vacio. AYUDA!:Se puede utilizar funcion len()
             -> tecnico: - Se debe seleccionar un tecnico de la lista de tecnicos. AYUDA!: Se puede usar la funcion de listar tecnicos.
                         - Al agregar el tecnico, se debe incrementar en uno en su lista de tecnicos.
                         IMPORTANTE!: Se debe crear un nuevo metodo para esta verificacion en el gestor.
        1.2) Al crear unicamente una instancia de Notebook es necesario:
             -> Logearlo (Escribir en una línea nueva: "numero_pc: descripcion_problema - tecnico"), 
                en un archivo llamado Notebook_a_arreglar.txt 
                IMPORTANTE!: Se debe crear un nuevo metodo en el mismo gestor.
                CUIDADO!: verificar permisos y extension.
    2.  Listar la lista de Computadoras, mostrando la informacion de cada instancia.
        AYUDA!: Hacer uso del metodo mostrar_informacion!.
    3.  Listar la Los tecnicos, mostrando nombre y la cant de pc que tienen a reparar.
        IMPORTANTE!. Recorrer lista_tecnicos.
        Ej.Bill Gates - 1
           Elon Musk  - 2
        
        
*   Se debe crear un main con un menu en un archivo distinto.   
*   Se deben crear los métodos correspondientes para las funciones del menú en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''

import GestorComputadoras as gc
gestor = gc.GestorComputadoras()


while True:
    condicion=input(
""" ------ MENU PRINCIPAL ------
Por favor ingrese una opcion:

        1. Agregar nueva computadora al sistema
        2. Listar computadoras en el sistema
        3. Listar tecnicos

        4. Salir
Numero : """)
    if (condicion=="1"): 
        gestor.crear_computadoras()
    elif (condicion=="2"):
        gestor.listar_computadoras()
    elif (condicion=="3"):
        gestor.mostrar_tecnicos()
    elif (condicion=="4"):
        print ("Gracias por usar el sistema")
        break
    else:
        print("ninguna opcion correcta")