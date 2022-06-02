"""
El programa debe:

pedir por teclado el dinero actual de una persona
pedir por teclado el precio del insumo que quiere comprar en USD
convertir ese dinero a dolares( 1USD -> 200$)
devoler por pantalla True en caso que pueda comprar, False en caso que no
No deben aparecer errores
"""

from os import putenv


try: 

    dinero_actual = float (input ("ingrese su denero actual: "))
    print(f"su dinero es {dinero_actual}")
    valor_insumo = float(input("ingrese el valor en USD de lo que desea comprar: "))
    dinero_actual_usd = dinero_actual/200
    print (dinero_actual_usd >= valor_insumo) 
    #Python por defecto te devuelve true o false.from xxxx import *

except: 
    print("Error en los datos colocados")

