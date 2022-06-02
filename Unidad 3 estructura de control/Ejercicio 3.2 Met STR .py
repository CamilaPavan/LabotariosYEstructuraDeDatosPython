"""
Almacenar una variable contraseña con una contraseña
Preguntar al usuario por la contraseña e imprimir 
por pantalla si la contraseña introducida por el 
usuario coincide o no con la variable 
IMPORTANTE: sin tener en cuenta mayúsculas y minúsculas.(metodos string)
no debe generar errores
"""

try:
    contrasena2 = "hola"
    constrasena = str(input("por favor ingrese una contrasena "))
    constrasena_min= constrasena.lower ()
    if constrasena_min == contrasena2:
        print (f"la contrasena es {constrasena_min}")
    else:
        print ("La contrasenia no es correcta")

except:
    print("por favor ingrese una contrasena valida")



variable_string="1234"
if variable_string.isdigit(): #lo ponemos con un punto y parentesis que abren y cierran 
  print("el stirng son solo numeros")
else:
  print("el stirng no son numeros")