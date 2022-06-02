import Funciones as fn

###**Ejercicio 4.1 (Calculadora)**


while True:
    condicion=input(
"""Por favor ingrese una opcion
        1. suma
        2. resta
        3. multiplicacion
        4. division
        5. Salir
Numero:  """)
    if (condicion=="1"): #lo comaparo en STR y no lo tengo que castear. 
        a,b = fn.pedir_numeros() #en las variables "a" y "b" se almacena los que retorna la funcion. 
        print (f"La suma de {a} + {b} = {fn.sumador(a,b)}")
    elif (condicion=="2"):
        a,b = fn.pedir_numeros()
        print (f"La resta de {a} - {b} = {fn.restador(a,b)}")
    elif (condicion=="3"):
        a,b = fn.pedir_numeros()
        print (f"La resta de {a} * {b} = {fn.multiplicador(a,b)}")
    elif (condicion=="4"):
        a,b = fn.pedir_numeros()
        if (a or b) == 0:
            print ("recorda que los numeros naturales no pueden dividirse en cero")
        else :
            print (f"la dividion entre {a} / {b} = {fn.divisor (a,b)}")
    elif (condicion=="5"):
        break
    else:
        print("ninguna opcion correcta")