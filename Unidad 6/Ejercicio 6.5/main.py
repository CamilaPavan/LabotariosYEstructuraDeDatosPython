"""
Ejercicio 6.5
Crear una clase padre Computadoras:

- Constructor debe incluir los atributos (id_modelo,listaPerifericos,SO)
- Crear metodos para esta clase de:
   Presentarse (id_modelo,listaPerifericos,SO)
   Indicar tipo de Computadora (Clases heredadas)
   Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO

Crear 2 clases que hereden de la clase padre Computadoras, con un atributo en particular para cada una
1. Escritorio
2. Notebbok

Crear clase GestorComputadora que cuente con las siguientes funciones para un menu

- Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
- Listar Computadoras (presentandolos), indicando tipo.
- Cambiar SO de una Computadora, verificando una lista de SO disponibles
- Listar perifericos

"""
import ClasesComputadoras as cp

lista_compu = []

pc_1 = cp.ComputadoraEscritorio("123", ["teclado", "mouse"], "CoreI5")
pc_2 = cp.Computadoras("123", ["teclado", "mouse"], "Windous")
pc_3 = cp.ComputadoraNotebook("123", ["teclado", "mouse"], "Linux")

lista_compu.append(pc_1)
lista_compu.append(pc_2)
lista_compu.append(pc_3)

for i in lista_compu:
    i.presentarse ()
    i.tipo_computadora()





