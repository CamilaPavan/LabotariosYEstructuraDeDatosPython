"""
Es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos.
Una clase hija puede sobreescribir los métodos o atributos, o incluso definir unos nuevos.
Se puede crear una clase hija con tan solo pasar como parámetro la clase de la que queremos heredar.

"""



class Animal: #padre
    pass

class Perro(Animal): #hij@
    pass

class Gato(Animal): #hij@
    pass

print(Perro.__bases__) #observamos de que clase padre hereda
print(Animal.__subclasses__())#observamos subclases de la clase padre
for i in Animal.__subclasses__():
  print(i)


class Animal:
    #contructor
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    #generico
    def hablar(self):
        pass
    #generico
    def tipo_animal(self):
        print("Soy un Animal del tipo", type(self).__name__)

class Perro(Animal):
    def hablar(self):
        print("Guau!")  #aca pongo especificamente que hace

class Gato(Animal):

    def hablar(self):
        print("Miau!")

    def rasgunar(self):
      print("Rasguño")

gato_1 = Gato("mamífero",5)
print(Gato.__bases__)
gato_1.hablar()
gato_1.tipo_animal()

#AGREGAR ALGO A LA CLASE HIJA, LLAMANDO AL CONSTRUCTOR DEL PADRE
class Animal:
    #contructor
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    #generico
    def hablar(self):
        pass
    #generico
    def tipo_animal(self):
        print("Soy un Animal del tipo", type(self).__name__)

class Perro(Animal):
    def __init__(self, especie, edad, raza):
        super().__init__(especie, edad) #Estos dos estan en la clase padre
        self.raza = raza #este es el que se agrega propio de la instacia

perro_1 = Perro("mamifero",5,"labrador")
perro_1.tipo_animal()