"""

Crear auto, indicando tipo de auto y guardar en una lista
Listar autos (presentandolos), indicando tipo de Vehiculo.
Cambiar velocidad de un Vehiculo
Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
"""

lista_autos = []
import Vehiculos as vh

class GestorAuto:
    def __init__(self):
        pass

    def crear_auto(self):
        #Tipo de auto
        while True:
            tipo_de_auto = input ("""
 ------ Menu principal tipo de vehiculos------
Por favor ingrese el vehiculo que desea crear
        1. Vehiculo generico
        2. Vehiculo particular
        3. Vehiculo Desportivo
        4. Vehiculo pickUp
Numero : """)
            if tipo_de_auto =="1" or  tipo_de_auto == "2" or tipo_de_auto == "3" or tipo_de_auto == "4":
                break               
            else:
                print ("opcion incorrecta")


        #(patente,marca,año,origen)
        patente = input ("ingrese la patente del vehiculo: ")
        marca = input ("ingrese la marca: ")
        while True:
            try:
                ano = int(input ("ingrese el ano de creacion: "))
                break
            except:
                print ("el ano debe ser numerico")

        origen = input ("ingrese el origen del vehiculo: ")

        if tipo_de_auto == "2" or tipo_de_auto == "3" or tipo_de_auto == "4":
            while True:
                try:
                    velocidad = (int(input("ingrese la velocidad del vehiculo: ")))
                    break
                except:
                    print ("la velocidad tiene que ser la cantidad de km que hace en una hora")

        instacia = patente
        if (tipo_de_auto == "1"):
            instacia = vh.Vehiculo (patente,marca, ano, origen)
            lista_autos.append (instacia)
        elif (tipo_de_auto == "2"):
            instacia = vh.vehiculo_particular (patente, marca, ano,origen,velocidad)
            lista_autos.append (instacia)
        elif (tipo_de_auto == "3"):
            instacia = vh.vehiculo_deportivo (patente, marca, ano,origen, velocidad)
            lista_autos.append (instacia)
        elif (tipo_de_auto == "4"):
            instacia = vh.vehiculo_pickup (patente, marca, ano,origen, velocidad)
            lista_autos.append (instacia)

    def presentar (self):
        for auto in lista_autos:
            auto.presentarse()
            auto.tipo_vehiculo()

    def cambiar_velocidad (self):
        print ("lista patentes: ")
        for auto in lista_autos:
            print (auto.patente)
        patente_auto = input ("ingrese la patente del vehiculo: ")
        for auto in lista_autos:
            if auto.patente == patente_auto:
                if(type(auto).__name__!="Vehiculo"):
                    while True:
                        try:
                            nueva_velocidad = int(input("ingrese la nueva velocidad: "))
                            auto.setear_velocidad_max (nueva_velocidad)
                            break
                        except:
                            print ("error en al velocidad")
                else:
                    print ("el vehiculo generico no tiene velocidad")

    def calcular_tiempo(self):
        print ("lista patentes: ")
        for auto in lista_autos:
            print (auto.patente)
        patente_auto= input ("ingrese la patente del vehiculo: ")
        for auto in lista_autos:
            if auto.patente == patente_auto:
                if(type(auto).__name__!="Vehiculo"):
                    while True:
                        try:
                            cantidad_de_km = int(input("ingrese la cantidad de km: "))
                            print (f"el tiempo en recorerr los {cantidad_de_km} km son {cantidad_de_km/auto.velocidad_max} horas")
                            break
                        except:
                            print ("los km son numericos")
                else:
                    print ("el vehiculo generico no tiene velocidad maxima")



        
        

