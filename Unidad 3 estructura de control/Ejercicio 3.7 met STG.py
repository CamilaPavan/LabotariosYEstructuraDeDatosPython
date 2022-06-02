"""
Ejercicio:
El programa debe :

Pedir al usuario un string
Determinar si una cadena esta en minusculas o mayusculas
"""

try: 
   var2= input (str("ingrese una cadena de texto "))
   if var2.islower():
       print ("la variable esta en minucula")


except:
    print("la cadena de texto no es correcta")

    #No puedo usar el else.