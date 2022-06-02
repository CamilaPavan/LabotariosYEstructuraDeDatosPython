"""
Cuyo constructutor debe inicializar los atributos tipo_de_figura, color, y tamaño (por defecto "pequeño")
"""


class FiguraGeometrica:
    #Crear la clase
    def __init__(self, tipo_de_figura,color,tamano="pequeno"):
        self.tipo_de_figura = tipo_de_figura
        self.color= color
        self.tamano=tamano

    #presentar
    def presentarse (self):
        print(f"soy una figura {self.tipo_de_figura}, de color {self.color} y mi tamano es {self.tamano}")

    #cambiar una atiburo
    def cambiar_color(self, color_nuevo):
        print(f"Cambie del color {self.color} al color {color_nuevo}")
        self.color = color_nuevo
    
    #si la figura es pequena la pasa a grande
    def verificar(self):
        if self.tamano == "pequeno":
           self.tamano = "grande" 
        print(f"El tamaño de la figura es {self.tamano}")

figura_1=FiguraGeometrica("triangulo","blanco")
figura_1.presentarse()
figura_1.cambiar_color("rojo")
figura_1.verificar()
