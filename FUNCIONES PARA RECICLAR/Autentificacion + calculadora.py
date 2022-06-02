"""Pedir usuario y contrasenia"""
def usuario_y_contrasena ():
    for i in range (3): #3 oportunidades. 
        usuario = input ("ingrese su usario: ")
        contra = input ("ingrese su contrana: ")
        if usuario == "user" and contra == "1234":
            return True
        else:
            print (f"usurio y contrasenia incorrecta, le quedan {2-i} oportunidades")
    return False

def sumador(a,b):
    suma = float(a)+float(b)
    return suma #podes poner el print aca y que no retorne nada. 

def restador(a,b):
    resta = float(a)-float(b)
    return resta

def divisor(a,b):
    try: 
        division = round(float(a)/float(b),2) #Aca en redondiar 
    except :
        print ("La division genero un error ")
        division= ("error")

    return division

def multiplicador(a,b):
    multiplicacion = float(a)*float(b)
    return multiplicacion

def pedir_numeros():
    while True: #Lo pongo aca para no usar "try" y "except" en todas las funciones 
        try:
            num1 = float(input("1° Argumento: "))
            num2 = float(input("2° Argumento: "))
            break
        except:
            print("argumentos incorrectos")

    return num1,num2 #Permite retornar mas de un argumento, Directamente separados con comas. 