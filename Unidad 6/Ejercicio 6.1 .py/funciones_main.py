import clases_presentarse as cp

lista_personas=[]

def crear_personas():
    while True: #pide DNI 
        dni= str(input("por favor ingrese su DNI"))
        if dni.isdigit():
            flag_agregar = True
            for persona in lista_personas:
                if dni == persona.dni:
                    print ("ese DNI ya existe")
                    flag_agregar = False
                    break #para salir del for
            if flag_agregar == True:
                break #el DNI Es valido 
        else:
            print("el DNI no es correcto")
    while True: #pido nombre
        nombre= str(input("por favor ingrese su nombre: "))
        if not nombre.isalpha():
            print("El nombre no puede tener numeros")
        else:
            break
    while True:#pido apeliido
        apellido = str(input("por favor ingrese su apellido: "))
        if not apellido.isalpha():
            print("El nombre no puede tener numeros")
        else:
            break
    while True: #edad
        try:
            edad = int(input("por favor ingrese su edad: "))
            if edad <= 0:
                print ("la edad debe ser positiva o mayor a cero: ")
            else:
                break
        except:
            print ("Error de argumentos")

    residencia= input("ingrese su domicilio: ")
    nombre_instacia = dni #que es el valor que nunca se repite. 
    nombre_instacia = cp.Persona (nombre, dni, apellido,edad,residencia) #Unico metodo que se llama a traves del archivo importado, el constructor
    lista_personas.append(nombre_instacia)

def listar_personas():
    for persona in lista_personas:
        persona.presentarse() #como todavia no lo recorre, no sabe que es un 
        #una instancia, por eso queda en blanco 


def consultar_rango():
    print("------ Lista de personas------")
    for persona in lista_personas:
        print(f"{persona.dni}\t{persona.nombre}\t{persona.apellido}\t{persona.edad}\t")
    while True: #pide dni
        dni_consultar = input("ingrese el dni a consultar")
        if dni_consultar.isdigit():
            for persona in lista_personas:
                if dni_consultar == persona.dni:
                    persona.rango_edad()
                    return
        else:
            print("el DNI no existe")
