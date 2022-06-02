#Funciones para resolver el ejercicio 4.5

dinero_disponible = 50000.0

"""ingresa dinero al sistema y actualiza el saldo"""
def ingresar_y_actualizar ():
    global dinero_disponible
    while True:
        try:
            dinero_ingresar = float(input("ingrese el dinero que ingresa a la cuenta: "))
            if dinero_ingresar > 0:
                break
        except: 
            print ("error en los parametros")
        
    
    dinero_disponible += dinero_ingresar
    return float (dinero_disponible)


"""Retirar el dinero, y actualiza el saldo"""
def retirar_y_actualizar():
    global dinero_disponible
    while True:
        try:
            dinero_retirar = float(input("ingrese el dinero que desea retirar: "))
            if dinero_retirar > 0 and dinero_retirar <= dinero_disponible:
                dinero_disponible -= dinero_retirar
                return (dinero_disponible)
            else:
                print("ingrese un valor valido")
        except: 
            print ("error en los parametros")



"""Dinero disponibles"""
def consultar_saldo ():
    global dinero_disponible
    print (f"el dinero disponible es {float(dinero_disponible)}")


"""Pedir usuario y contrasenia"""
def usuario_y_contrasena ():
    for i in range (3):
        usuario = input ("ingrese su usario: ")
        contra = input ("ingrese su contrana: ")
        if usuario == "user" and contra == "1234":
            return True
        else:
            print (f"usurio y contrasenia incorrecta, le quedan {2-i} oportunidades")
    return False

    
    

            