"""
Cuyo constructutor debe inicializar los atributos 
nombre, 
apellido, 
edad, 
ciudad_de_residencia

Niño (0 a 14), Adolecente (14 a 22), Joven (22 a 30), mayor(30 a 50), mas mayor(50 a 120)
"""


class Persona:
    nacionalidad = "argentina" #global, se usa el creador 
    def __init__(self,dni, nombre1, apellido1, edad1, residencia1):
        self.dni=dni #unico
        self.nombre=nombre1 #este crea los atributos 
        self.apellido=apellido1
        self.edad=edad1
        self.residencia=residencia1
        

    def presentarse(self):
        print(f"soy {self.nombre}{self.apellido}, tengo {self.edad} y vivo en {self.residencia}")

    def rango_edad(self):
        if self.edad >=0 and self.edad <=14 :
            print(f"{self.nombre}es un nino")
        elif self.edad >14 and self.edad <=22:
                print(f"{self.nombre}es un adolecente")
        elif self.edad >22 and self.edad <=30:
                print(f"{self.nombre}es un Joven")
        elif self.edad >30 and self.edad <=50:
            print(f"{self.nombre}es un mayor")
        elif self.edad >50 and self.edad <=120:
            print(f"{self.nombre}es un mas mayor")
        else:
            print("erro en la edad")