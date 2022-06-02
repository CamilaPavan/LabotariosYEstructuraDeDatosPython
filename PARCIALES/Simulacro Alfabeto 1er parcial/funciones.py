
alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#1. Mostrar el alfabeto A
def mostrar_alfabeto_A():
    global alfabeto_a
    for i in alfabeto_a:
        print (i,end= "," ) 
        

#2.Mostrar el alfabeto B
def mostrar_alfabeto_B():
    global alfabeto_b
    for i in alfabeto_b:
        print (i,end= ",")


#3.Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma)
#NO LA MODIFICA, LA AGREGA
def modificar_letra():
    global alfabeto_a
    global alfabeto_b
    while True:
        letra_a_modificar = input("ingrese la letra a modificar: ")
        if letra_a_modificar in alfabeto_a:
            letra_nueva = input("ingrese la nueva letra: ")
            lugar = alfabeto_a.index(letra_a_modificar)
            alfabeto_a.insert(lugar,letra_nueva)
            alfabeto_a.index[(letra_a_modificar)]= letra_nueva
            letra_alf_b = input ("ingrese la nueva letra para el abecedario B: ")
            alfabeto_b.insert(lugar, letra_alf_b)
            mostrar_alfabeto_A() 
            mostrar_alfabeto_B()
            return

        elif letra_a_modificar in alfabeto_b:
            letra_nueva = input("ingrese la nueva letra: ")
            lugar = alfabeto_b.index(letra_a_modificar)
            alfabeto_b.insert(lugar,letra_nueva)
            letra_alf_a = input ("ingrese la nueva letra para el abecedario A: ")
            alfabeto_a.insert(lugar, letra_alf_a)
            mostrar_alfabeto_B()
            mostrar_alfabeto_A() 
            return
        else:
            print("la letra no se encuentra en el abecedario")

#Conversion de alfabeto A a alfabeto B
def de_alfabetoA_a_B():
    global alfabeto_a
    global alfabeto_b
    frase_nueva = []
    while True:   
        palabra_a_convertir = input("ingrese las letras a modificar: ")
        lista_palabra_a_convertir =list(palabra_a_convertir) 
        try:
            for i in lista_palabra_a_convertir:
                lugar= alfabeto_a.index(i)
                letra_en_otro_abc = alfabeto_b[lugar]
                frase_nueva.append(letra_en_otro_abc)
            break
        except:
            print("las letras no se encuentran en el abecedario")
    print (f"resultado: {frase_nueva}")


#Conversion de alfabeto B a alfabeto A
def de_alfabetoB_a_A():
    global alfabeto_a
    global alfabeto_b
    frase_nueva = []
    while True:   
        palabra_a_convertir = input("ingrese las letras a modificar: ")
        lista_palabra_a_convertir =list(palabra_a_convertir) 
        try:
            for i in lista_palabra_a_convertir:
                lugar= alfabeto_b.index(i)
                letra_en_otro_abc = alfabeto_a[lugar]
                frase_nueva.append(letra_en_otro_abc)
            break
        except:
            print("las letras no se encuentran en el abecedario")
    print (f"resultado: {frase_nueva}")

#Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B)
def vereficar_existencia():
    
    opcion = input("""Elija alfabeto:
                        1. minuscula
                        2. MAYUSCULA
                numero:   """)
    if opcion == "1":
        letra_a_chequear = input ("digite la letra a chequear: ")
        if letra_a_chequear in alfabeto_a:
            print ("la letra si se encuentra en el abecedario")
        else:
            print ("la letra no se encuentra en el abecedario")
    elif opcion == "2":
        letra_a_chequear = input ("digite la letra a chequear: ")
        if letra_a_chequear in alfabeto_b:
            print ("la letra si se encuentra en el abecedario")
        else:
            print ("la letra no se encuentra en el abecedario")
            
    else:
        print("opcion incorrecta")

