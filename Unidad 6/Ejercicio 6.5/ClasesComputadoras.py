"""
- Crear metodos para esta clase de:
   Presentarse (id_modelo,listaPerifericos,SO)
   Indicar tipo de Computadora (Clases heredadas)
   Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO

Crear 2 clases que hereden de la clase padre Computadoras, con un atributo en particular para cada una
1. Escritorio
2. Notebbok

"""

#(id_modelo,listaPerifericos,SO)

lista_perificos = [list]

class Computadoras ():
    def __init__(self,id_modelo1, listaPerifericos1, SO1):
        self.id_modelo = id_modelo1
        self.listaPerifericos = listaPerifericos1
        self.SO = SO1
    
    def presentarse (self):
        print (f"""soy una computadora modelo {self.id_modelo} , tengo {self.listaPerifericos}
        y tengo de sistema operativo {self.SO}""")

    def tipo_computadora(self):
        print("Soy una computadora del tipo", type(self).__name__)

        #modifica clase hija
    def agregar_perifericos (self):
        pass
        #modifca clase hija
    def cambiar_SO (self):
        pass

class ComputadoraEscritorio (Computadoras):
    def __init__(self, id_modelo1, listaPerifericos1, SO1, escritorio=0 ):
        super().__init__(id_modelo1, listaPerifericos1, SO1)
        self.escritorio = escritorio

    def agregar_perifericos(self, nuevo_periferico):
        print (f"Los periféricos que tiene la Computadora de Escritorio son {self.listaPerifericos}")
        self.listaPerifericos.append(nuevo_periferico)
        return super().agregar_perifericos()

    def CambiarSO(self,nuevo_SO):
        print (f"El SO de la computadora Escritorio era {self.SO} y ahora es {nuevo_SO}")
        self.SO = nuevo_SO

class ComputadoraNotebook (Computadoras):
    def __init__(self, id_modelo1, listaPerifericos1, SO1, notebook=0 ):
        super().__init__(id_modelo1, listaPerifericos1, SO1)
        self.notebook = notebook
    
    def agregar_perifericos(self, nuevo_periferico):
        print (f"Los periféricos que tiene la Computadora de Escritorio son {self.listaPerifericos}")
        self.listaPerifericos.append(nuevo_periferico)
        return super().agregar_perifericos()

    def CambiarSO(self,nuevo_SO):
        print (f"El SO de la computadora Escritorio era {self.SO} y ahora es {nuevo_SO}")
        self.SO = nuevo_SO
