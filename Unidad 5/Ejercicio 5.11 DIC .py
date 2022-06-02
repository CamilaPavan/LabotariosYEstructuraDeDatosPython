"""Crear una funcion que debe: (usar diccionario)

Contener un diccionario con distintas monedas de paises, siendo: La key el nombre de la moneda y el valor el simbolo.
Preguntar al usuario que tipo de moneda desea y mostrar el simbolo si existe en el diccionario, caso contrario indicar que no existe.
"""

monedas = {
    "Peso":"$", 
    "Dolar": "USD",
    "Euro":  "€"
    }

def obtener_simbolo():
  moneda = input("Ingrese que tipo de moneda desea saber el simbolo: ").capitalize() #para poner la primera letra en mayuscula
  print(moneda)
  if moneda in monedas:
    print(f"El simbolo de {moneda} es {monedas[moneda]}")
  else:
    print("La moneda no existe en el diccionario")

def obtener_simbolo_2():
  moneda_a_saber = input("Ingrese que tipo de moneda desea saber el simbolo: ").capitalize()
  valor = monedas.get(moneda_a_saber,"No existe") #le paso pa clave, y si no existe, devuelve el  valor que le pones entre comillas
  print(f"El simbolo de {moneda_a_saber} : {valor}")


obtener_simbolo_2()
