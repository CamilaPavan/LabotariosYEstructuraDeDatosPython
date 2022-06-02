"""
El programa va tener una  clase auto con , los siquientes atributos:
Color
Marca
Modelo
Patente #Unico
"""



class autos:
    nacionalidad = "Argentina"
    def __init__(self, color1, marca1, anio1, patente1):
        self.color = color1
        self.marca = marca1
        self.anio = anio1
        self.patente = patente1

    def presentarse (self):
        print (f" el auto {self.marca}, es de color {self.color} y su patente es {self.patente}")

    def rango_edad (self):
        if self.anio <= 2000 :
            print (f"El auto {self.marca} es viejo")
        elif self.anio >2000 and self.anio <=2010:
            print (f"El auto {self.marca} es medio ")
        elif self.anio > 2010 and self.anio <= 2022:
            print (f"El auto {self.marca} es NUEVO")
        else:
            print ("Ese auto todavia no existe")
