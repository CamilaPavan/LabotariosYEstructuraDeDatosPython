"""
El programa debe:

Contar con 3 funciones:
    1.Contador de letras (letra,palabra): Debe contar la cantidad de letras que tiene una palabra o frase (Ambos parametros)
    2.Comparador de palabras (palabra1 vs palabra2): debe comparar que palabra tiene mas letra.IMPORANTE:deben ser palabras y no frases (verificar)
    3.Quitador de vocales(palabra a retirar las vocales): debe recibir una palabra o frase y quitar todas las vocales
Contar con un menu donde debe pedir al usuario que operacion realizar
Pedir los parametros y devolver el resultado al usuario
Gestionar posibles errores
"""

def contador_de_letras(letra,palabra_o_frase):
    palabra_o_frase
    contador = 0
    for i in palabra_o_frase:
        if i == letra:
            contador += 1
    return contador


def comparador_de_palabras(palabra1,palabra2):
    contador1= 0
    contador2= 0
    for i in palabra1:
        contador1+= 1
        if i == " ":
            return(print ("ingreso una frase"))
        
    for i in palabra2:
        contador2 += 1
        if i == " ":
            return(print("ingreso una frase, no una palabra"))

    if contador1 < contador2:
        print (f"la palabra {palabra1} es mas corta que {palabra2}")
    else:
        print (f"la palabra {palabra1} es mas larga que {palabra2}")


def quitador_de_vocales(palabra_o_frase):
    palabra_auxiliar = ""
    for i in palabra_o_frase:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            palabra_auxiliar= palabra_auxiliar + i

    print (palabra_auxiliar)



while True:
    condicion=input(
""" ------ MENU PRINCIPAL ------
Por favor ingrese una opcion
        1. contador de letras
        2. comparar palabras
        3. Quitar vocales
        4. Salir
Numero : """)
    if (condicion=="1"): 
        letra = input("ingrese la letra a contar: ")
        frase = input ("ingrese la frase: ")
        print (f"la letra se repite {contador_de_letras(letra,frase)} veces ")
    elif (condicion=="2"):
        palabra1 = input("ingrese la primer palabra a comparar: ")
        palabra2 = input ("ingrese la segunda palabra a comparar: ")
        comparador_de_palabras(palabra1, palabra2)
    elif (condicion=="3"):
        palabra_o_frase = input ("ingrese la palabra o frase a quitar las vocales: ")
        quitador_de_vocales (palabra_o_frase)
    elif (condicion=="4"):
        print ("Gracias por usar .....")
        break 
    else:
        print("ninguna opcion correcta")






