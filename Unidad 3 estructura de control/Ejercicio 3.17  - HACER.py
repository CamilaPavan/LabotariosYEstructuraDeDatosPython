"""
TAREA:
El programa debe:
*    Pedir al usuario cantidad de personas
*    Pedir al usuario una a una la edad de las personas
*    Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
*    no deben generar errores
"""



while True:
    try: 
        while True:
            cantidad_de_personas = int(input("Ingrese la cantidad de personas: "))
            if cantidad_de_personas > 0:
                break
            else:
                print ("por favor ingrese un numero mayor a cero")
    except:
        print ("ingrese un numero")

    edad_mayor=0
    for i in range (1,cantidad_de_personas+1):
        try:
            while True:
                edad= float(input(f"ingrese la edad de la persona {i}: "))
                if edad>0:
                    break
            if edad > edad_mayor:
                edad_mayor=edad
        except:
            print("ingreso incorrectamente la edad")
    print (f"la edad de la persona mayor es {edad_mayor}")
    break

        