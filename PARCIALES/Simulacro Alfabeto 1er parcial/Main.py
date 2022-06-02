"""
**Ejercicio 5.10 (Conversión de alfabeto)**
El programa debe:
*   Simular la conversion de un alfabeto a otro: Por ejemplo el moorse 
    (NO ES ESTRICTAMENTE NECESARIO USAR ESTE ALFABETO, PUEDE SER INVENTADO)

```
 alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]
```

*   Contar con 6 funciones disponibles en el menu:
    1. Mostrar el alfabeto A
    2. Mostrar el alfabeto B
    3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma)
    4. Conversion de alfabeto A a alfabeto B: ejemplo **abc --> .--...-.-.**
    5. Conversion de alfabeto B a alfabeto A: ejemplo **.--...-.-. --> abc**
    6. Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B)

*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
    """
    
import funciones as fn

while True:
    condicion=input(
""" ------ MENU PRINCIPAL ------
Por favor ingrese una opcion
        1. Mostrar alfabeto A
        2. Mostrar alfabeto B
        3. Modificar letra en ambos alfabetos
        4. Convertir de alfabeto A a alfabeto B
        5. Convertir de alfabeto B a alfabeto A
        6. Verificar la existencia de una letra
        7. salir
Numero : """)
    if (condicion=="1"): 
        fn.mostrar_alfabeto_A()
    elif (condicion=="2"):
        fn.mostrar_alfabeto_B()
    elif (condicion=="3"):
        fn.modificar_letra()
    elif (condicion=="4"):
       fn.de_alfabetoA_a_B()
    elif (condicion == "5"):
        fn.de_alfabetoB_a_A()
    elif (condicion == "6"):
        fn.vereficar_existencia()
    elif (condicion=="7"):
        print ("Gracias por usar el programa")
        break 
    else:
        print("ninguna opcion correcta")



