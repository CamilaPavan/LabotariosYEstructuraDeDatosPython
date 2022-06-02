"""
*   Contar con una Clase Evento con los atributos (nombre_evento (único), fecha, hora, lugar)
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo más:
        - EventoPersonal (Atributo: organizador (nombre de la grupo que organiza))
        - EventoLaboral (Atributo: obligatorio "True o False" (por defecto = True))
        
*   Se deben crear 4 métodos para la clase padre Evento (que heredaran las clases hijas):
        1. Mostrar información: Que indique el nombre_evento, fecha y lugar del evento 
        2. Obtener tipo de evento (tipo de clases heredadas o padre)
        3. Setear Fecha y Hora (Setearán la Fecha y Hora en una misma función)
        4. Setear lugar (Setear el lugar)
"""

class Evento: #Clase padre
    def __init__(self,nombre_evento,fecha,hora,lugar): #constructor + atributos
        self.nombre_evento =nombre_evento
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar
    
    def mostrar_info(self): #Metedos para las clases
        print(f"Nombre del Evento: {self.nombre_evento} - Fecha y hora: {self.fecha} {self.hora} - Lugar del evento: {self.lugar}")

    def tipo_evento(self): #Metodos para las clases
        print(f"Evento tipo {type(self).__name__}") #Tipo de evento con el type
    
    def set_fecha_hora(self,hora,fecha): #metodos para la clase , para setear se tiene que llamar igual al atributo
        self.hora=hora
        self.fecha=fecha
        
    def set_lugar(self,lugar): #Metodos para la clase
        self.lugar=lugar
    
    def get_nombre(self): #metodos para la clase , lo agregamos para el gestor
        return self.nombre_evento
        
class EventoPersonal(Evento): #Clase hija
    def __init__(self, nombre_evento, fecha, hora, lugar,organizador):
        super().__init__(nombre_evento, fecha, hora, lugar) #super los atributos que tienen aparte
        self.organizador = organizador

class EventoLaboral(Evento): #Clase hija
    def __init__(self, nombre_evento, fecha, hora, lugar, obligatorio = True): #oblitatorio es un TRUE.
        super().__init__(nombre_evento, fecha, hora, lugar)
        self.obligatorio = obligatorio