while True:
    condicion=input(
""" ------ MENU PRINCIPAL ------
Por favor ingrese una opcion
        1. x
        2. x
        3. x
        4. x
        5. Salir
Numero : """)
    if (condicion=="1"): 
        pass 
    elif (condicion=="2"):
        pass
    elif (condicion=="3"):
        pass
    elif (condicion=="4"):
       pass
    elif (condicion=="5"):
        print ("Gracias por usar .....")
        break 
    else:
        print("ninguna opcion correcta")


while True:
    opcion =input("""
    ------ menu principal-----
    1. x
    2. x
    3. x
    4. Salir
    opcion: """) 
    if (opcion=="1"): 
        pass
    elif (opcion=="2"):
        pass
    elif (opcion=="3"):
        pass
    elif (opcion=="4"):
        break
    else:
        print("Opcion incorrecta")

#Menu comparando que los int, sean int:

try:
    dato_1 = input("""Por favor ingrese una opcion
    - imprimir
    - 1
    - 2
    - salir
    ingreso : """)
    if dato_1.isalpha(): #si el dato es alfabetico
        if dato_1=="imprimir":
            print("ingresaste IMPRIMIR")
        elif dato_1=="salir":
            print("ingresaste SALIR")
        else:
            print("no ingresaste una opcion alfanumerica correcta")
    elif dato_1.isdigit(): #si el dato es numerico
        if int(dato_1)==1:
            print("ingresaste 1")
        elif int(dato_1)==2:
            print("ingresaste 2")
        else:
            print("no ingresaste una opcion numerica correcta")
    else:
        print("ingresaste numeros y letras muy mal")
except:
    print("ERROR")