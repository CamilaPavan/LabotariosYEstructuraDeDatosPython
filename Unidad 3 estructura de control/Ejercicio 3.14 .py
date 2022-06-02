"""
El programa debe:

Preguntar al usuario una cantidad a invertir
Preguntar al usuario el interés anual y el número de años
Mostrar por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
while True:
    try:
        inversion = float(input("ingrese el valor a invertir: "))
        interes = float(input("ingrese el interes anual: "))
        tiempo = int (input("coloque la cantidad de anios: "))
        break
    except:
        print ("uno de los valores no fue correcto, por favor intete de nuevo")

for i in range (1,tiempo+1):
    inversion+= inversion*interes/100
    print (f"el dinero obteniedo en el anio {i} es igual a {inversion}")