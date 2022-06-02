"""
*   La Clase auto tiene los atributos (patente, modelo, año, marca, nombre_Chofer (objeto clase Choferes))
    2. Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
    3. Modificar el chofer de un auto
    6. imprimir lista de autos (con toda su informacions)
"""
class Auto:
    def __init__(self,patente,modelo,anio,marca,dni_chofer):
        self.patente = patente
        self.modelo = modelo
        self.anio = anio
        self.marca = marca
        self.dni_chofer = dni_chofer
    
    def get_chofer(self):
        return self.dni_chofer

    def get_patente(self):
        return self.patente
    
    def set_chofer(self,dni_chofer):
        self.dni_chofer = dni_chofer
    
    def imprimir_info(self):
        print(f"Patente: {self.patente} - año: {self.anio} - marca/modelo: {self.marca}/{self.modelo} - Chofer: {self.dni_chofer}")