


class Computadora ():
    def __init__(self,num_pc,descripcion,tecnico):
        self.num_pc = num_pc #atributo unico
        self.descripcion_problema = descripcion
        self.tecnico = tecnico

    def set_descripcion (self,problema):
        self.descripcion_problema = problema
        print (f"el prblema de la maquina {self.num_pc} es {self.descripcion_problema}")

    def get_descripcion (self):
        return self.descripcion_problema

    def set_tecnico (self, tecnico_nuevo):
        self.tecnico = tecnico_nuevo
        print (f"el tecnico de la pc {self.num_pc} es {self.tecnico}")
    
    def get_tecnico (self):
        return self.tecnico

    def get_tipo_clase (self):
        return (type(self).__name__)

    def mostrar_informacion(self):
        print (f"""La computadora con numero: {self.num_pc} 
No funciona porque: {self.descripcion_problema} 
Tecnico a cargo: {self.tecnico}""")




class Notebook (Computadora):
    def __init__(self, num_pc, descripcion, tecnico):
        super().__init__(num_pc, descripcion, tecnico)

pc_1 = Computadora(15,"hola","casa")
pc_2 = Notebook(15,"hola","casa")

print(f" la pc es del tipo {pc_2.get_tipo_clase()}")
print(f"{pc_2.get_descripcion()}")
        