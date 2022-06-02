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
    
    #si un atributo es de una forma, pasarlo a otro
    def verificar(self):
        if self.tamaño == "pequeño":
         self.tamaño = "grande"
        print(f"El tamaño de la figura es {self.tamaño}")

    #verificar un pametro que existe con unos nuevo, si es mas o menos viejo 
    def verificar_año(self,año_comparar):
        if self.año < año_comparar: #recomendable no agregar datos
            print("El año es mayor")
        elif self.año == año_comparar:
            print("El año es igual")
        elif self.año > año_comparar:
            print ("El año es menor")
