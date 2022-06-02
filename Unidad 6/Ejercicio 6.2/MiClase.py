"""
Cuyo constructutor debe inicializar los atributos tipo_de_figura, color, y tamaño (por defecto "pequeño")
"""




lista_figuras=[]

class FiguraGeometrica:
    def __init__(self, tipo_de_figura1, color1, tamano1 = "pequeno"):
        self.tipo_de_figura= tipo_de_figura1
        self.color = color1
        self.tamano = tamano1 #Primero el nombre 
    
    def listar (self):
        print (f" soy un {self.tipo_de_figura} de color {self.color} y mido {self.tamano}")

    def cambiar_color (self,nuevo_color1):
        print (f"cambie de color {self.color} y ahora soy {nuevo_color1}")
        self.color=nuevo_color1

    def verificar_tamano (self):
        if self.tamano == "pequeno":
            self.tamano = "grande"
        print(f"soy de tamano {self.tamano}")





figura_1 = FiguraGeometrica ("circulo", "azul" ,"mediano")
figura_2 = FiguraGeometrica("cuadrado", "rojo" )

figura_2.cambiar_color("MAGENTA")
figura_1.listar()
figura_2.verificar_tamano() #si me hace el cambio
figura_1.verificar_tamano() #este no, porque es mediano

        