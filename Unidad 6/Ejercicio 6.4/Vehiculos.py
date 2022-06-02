"""
Constructor debe incluir los atributos (patente,marca,año,origen)
Crear metodos para esta clase de:
Presentarse (patente,marca,año,origen)
Indicar tipos de vehiculo(Clases heredadas)
Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, 
obtener_velocidad, setear_velocidad
"""

class Vehiculo:
    def __init__(self,patente1,marca1,anio1,origen1):
        self.patente = patente1
        self.marca = marca1
        self.anio = anio1
        self.origen = origen1

    def presentarse (self):
        print (f"soy un vehiculo con patente {self.patente}, marca {self.marca} del anio {self.anio} y de origen {self.origen}")

    def tipo_vehiculo(self):
        print("Soy un auto del tipo", type(self).__name__)

    def acelerar (self):
        pass #porque lo modifica la clase hija

    def desacelerar (self):
        pass 

    def retroceder (self):
        pass 

    def obtener_velocidad_max(self):
        pass 

    def setear_velocidad_max (self):
        pass 


class vehiculo_particular (Vehiculo):
    def __init__(self, patente1, marca1, anio1, origen1, velocidad_maxima1=120):
        super().__init__(patente1, marca1, anio1, origen1)
        self.velocidad_max = velocidad_maxima1

    def acelerar_hijo(self):
        print (f"estoy acelerando {self.tipo_vehiculo}")

    def desacelerar(self):
        print (f"estoy desacelerando {self.tipo_vehiculo}")
        return super().desacelerar()
    
    def retroceder(self):
        print (f"estoy retrocediendo {self.tipo_vehiculo}")
        return super().retroceder()
    
    def obtener_velocidad_max(self):
        print (f"mi velocidad maxima es {self.velocidad_max}")
        return super().obtener_velocidad_max()
    
    def setear_velocidad_max(self,velocidad):
        self.velocidad_max = velocidad
        print (f"mi nueva velocidad es {velocidad}")
        return super().setear_velocidad_max()

class vehiculo_pickup (Vehiculo):
    def __init__(self, patente1, marca1, anio1, origen1, velocidad_maxima1=110):
        super().__init__(patente1, marca1, anio1, origen1)
        self.velocidad_max = velocidad_maxima1

    def acelerar_hijo(self):
        print (f"estoy acelerando {self.tipo_vehiculo}")

    def desacelerar(self):
        print (f"estoy desacelerando {self.tipo_vehiculo}")
        return super().desacelerar()
    
    def retroceder(self):
        print (f"estoy retrocediendo {self.tipo_vehiculo}")
        return super().retroceder()
    
    def obtener_velocidad_max(self):
        print (f"mi velocidad maxima de {self.tipo_vehiculo} es {self.velocidad_max}")
        return super().obtener_velocidad_max()
    
    def setear_velocidad_max(self,velocidad):
        self.velocidad_max = velocidad
        print (f"mi nueva velocidad es {velocidad}")
        return super().setear_velocidad_max()

class vehiculo_deportivo (Vehiculo):
    def __init__(self, patente1, marca1, anio1, origen1, velocidad_maxima1=210):
        super().__init__(patente1, marca1, anio1, origen1)
        self.velocidad_max = velocidad_maxima1

    def acelerar_hijo(self):
        print (f"estoy acelerando {self.tipo_vehiculo}")

    def desacelerar(self):
        print (f"estoy desacelerando{self.tipo_vehiculo}")
        return super().desacelerar()
    
    def retroceder(self):
        print (f"estoy retrocediendo {self.tipo_vehiculo}")
        return super().retroceder()
    
    def obtener_velocidad_max(self):
        print (f"mi velocidad maxima de {self.tipo_vehiculo} es {self.velocidad_max}")
        return super().obtener_velocidad_max()
    
    def setear_velocidad_max(self,velocidad):
        self.velocidad_max = velocidad
        print (f"mi nueva velocidad es {velocidad}")
        return super().setear_velocidad_max()


