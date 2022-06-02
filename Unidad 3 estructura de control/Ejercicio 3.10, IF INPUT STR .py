"""
El programa debe:

pedir un dato al usuario
solo en caso que este escriba la palabra clave "python" imprimir por pantalla "Correcto", en caso contrario debe seguir pidiendo el dato
no deben aparecer errores.
"""
flag = True
while flag: 
    if input("por favor coloque la palabra clave ")  == "phyton": #Se puede hacer el input dentro del IF, sin definir la variable. 
        print("Correcto")
        flag = False
    else: 
        print("no ingreso la palabra correcta, intentelo nuevamente ")


