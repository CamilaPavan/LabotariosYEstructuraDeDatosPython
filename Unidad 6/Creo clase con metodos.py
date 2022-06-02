class Lapiz:
    
    def __init__(self, color = "blanco", longitud = 3): #Se pasa por defecto, si no aclara, toma ese valor 
      print(f"Creando un lapiz de color {color}, que mide {longitud} cm")
      # Atributos de instancia
      self.color = color
      self.longitud = longitud
    
    def cambio_de_color(self,color):
      self.color = color

    def mostrar_info(self):
       print(f"El lapiz es de color {self.color} y mide {self.longitud} cm")

lapices = [] # lista vacia
while True:
    nombre_variable = input("Ingrese el nombre de un objeto lapiz o (listo): ")
    if nombre_variable == "listo":
        break
    nombre_variable = Lapiz("rojo",10) #creo un objeto de la clase lapiz
    lapices.append(nombre_variable) #Guardo el objeto en una lista

#recorro la lista
for lapiz in lapices:
  lapiz.mostrar_info()