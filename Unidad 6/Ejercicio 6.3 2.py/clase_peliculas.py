"""
Se deben crear 4 metodos en la clase:
Presentar la pelicula: La pelicula {nombre} de {genero}
 del {año} obtuvo una puntuacion de {puntuacion} y fue filmada en {nacionalidad}
"""



class Pelicula:
    def __init__(self,nombre1,genero1,ano1, puntuacion1,nacionalidad1):
        self.nombre = nombre1 #unico
        self.genero= genero1
        self.ano=ano1
        self.puntuacion = puntuacion1
        self.nacionalidad = nacionalidad1

    def presentar (self):
        print (f"""La pelicula {self.nombre}, de {self.genero} del {self.ano} obtuvo una puntuacion de {self.puntuacion}
        y fue filmada en {self.nacionalidad}""")

    #Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
    def comparar_ano (self,ano1):
        if self.ano < ano1:
            print(f"La pelicula es mayor al ano {ano1}, se creo en {self.ano}")
        elif self.ano == ano1:
            print(f"La pelicula, se creo en el mismo ano {self.ano}")
        else:
            print(f"la pelicula es menor, se creo en {self.ano}")

    #Modificar puntuacion de la pelicula (entre 1 y 10)
    def modificar_puntuacion (self,puntuacion_nueva):
        if puntuacion_nueva != self.puntuacion:
            print (f"la puntacion de la pelicula {self.nombre} se cambio de {self.puntuacion} a {puntuacion_nueva}")
            self.puntuacion = puntuacion_nueva
        else:
            print("la pelicula ya tenia esa puntuacion")
    
    #Modificar el genero de la pelicula
    def modificar_genero (self,genero_nuevo):
        if genero_nuevo != self.genero:
            print (f"El genero de la pelicula {self.nombre} se cambio de {self.genero} a {genero_nuevo}")
            self.genero = genero_nuevo
        else:
            print("la pelicula ya tenia ese genero")





