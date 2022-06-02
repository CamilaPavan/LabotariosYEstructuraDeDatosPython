"""
*   Contar con 4 funciones:
  1.  Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
  2.  Conversor de cm3 a litros (cantidad de cm3)
  3.  Conversor de litros a cm3 (cantidad de litros)
  4.  Pesos a Dolares (pesos)
*   Contar con un menu donde debe pedir al usuario que operacion realizar
*   Pedir los parametros y devolver el resultado al usuario
*   Gestionar posibles errores
"""



def grados_a_fahrenheit():
    while True:
        try:
            grados = float(input("ingrese los grados que desea convertir: "))
            break
        except:
            print ("Error, vuelva a colocar el valor numerico")
    print(f"los {grados} grados son {round(grados*1.18+32,2)} grados Fahrenheit")

def cm3_a_litros ():
    while True:
        try:
            cm3= float(input("por favor coloque el numero de centrimetros cubicos que desea convertir: "))
            break
        except:
            print ("error, por favor coloque nuevamente el valor")
    print (f"los {cm3} cm3 son {cm3 *0.001} litros")

def litros_a_centrimetros ():
    while True:
        try:
            litros= float(input("por favor coloque el numero de litros que desea convertir: "))
            break
        except:
            print ("error, por favor coloque nuevamente el valor")
    print (f"los {litros} litros son {litros/0.001} cm3")

def pesos_a_dolares():
    while true:
        try:
            pesos=float(input("ingrese la cantidad de pesos a convertir: "))
            break
        except:
            print ("error, ingrese nuevamente")
    print(f" ${pesos} = {round(pesos/220,2)} USD")

while True:
    condicion=input(
"""Por favor ingrese una opcion
        1. Conversor de Grados Celcius a Fahrenheit
        2. convertir de cm3 a litros
        3. convertir de litros a cm3
        4. Convertir de pesos a dolares
        5. Salir
Numero : """)
    if (condicion=="1"): 
        grados_a_fahrenheit()
    elif (condicion=="2"):
        cm3_a_litros()
    elif (condicion=="3"):
        litros_a_centrimetros()
    elif (condicion=="4"):
       pesos_a_dolares ()
    elif (condicion=="5"):
        break
    else:
        print("ninguna opcion correcta")