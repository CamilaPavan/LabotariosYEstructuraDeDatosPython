""""
Simular cajero automatico y pedir usuario y contraseña (user, 1234) caso verdadero mostrar menu y en caso falso seguir pidiendo.
En caso de mal ingreso de usuario o contraseña 3 veces el programa debe detenerse
El menu debe mostrar las funciones posteriores.
Contar con 4 funciones:
Consultar el saldo (inicio de 50000)
Ingresar dinero y actualizar saldo
Retirar dinero y actualizar saldo
Salir, y volver al menu de usuario y contraseña
Gestionar posibles errores

CLASE 10 todo perfecto. 
"""


import funciones_saldos as fn
import funcion_autentificacion as fa
dinero_disponible = 50000


condicion= True
while condicion:
    condicion = fa.usuario_y_contrasena()

    opcion =input(
"""Por favor ingrese una opcion
        1. consultar saldo
        2. Ingresar dinero
        3. Retirar dinero y actualizar saldo
        4. Salir
Numero : """)
    if (opcion=="1"): 
        fn.consultar_saldo()
    elif (opcion=="2"):
         print(f"el dinero disponible en la cuenta es de {fn.ingresar_y_actualizar()}")
    elif (opcion=="3"):
         print(f"el dinero disponible en la cuenta es de {fn.retirar_y_actualizar()}")
    elif (opcion=="4"):
        break
    else:
        print("ninguna opcion correcta")
    
    condicion = True