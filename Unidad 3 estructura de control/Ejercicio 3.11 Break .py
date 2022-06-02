"""
mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
si el usuario escribe "hola" o "chau" que no se haga el eco
"""



while True:
    palabra=str(input("ingrese una palabra:"))  
    if palabra == "salir":
        print(palabra)
        break
    elif palabra == "hola" or palabra == "chau":
        continue
    else:
        print(palabra)