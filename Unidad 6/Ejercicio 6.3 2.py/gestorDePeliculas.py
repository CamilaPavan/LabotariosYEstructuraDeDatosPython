#Funciones de main, ejercicio 6.3 Peliculas

#1. Crear una pelicula y guardar su nombre en una lista de peliculas
#nombre, genero, año,puntuacion,nacionalidad


import clase_peliculas as cp
lista_peliculas = []
generos = ["terror" , "comedia" , "suspenso", "biografia", "romantica"]

class gestorDePeliculas:
    def __init__(self) :
        pass

    def verificar_pelicula (self,pelicula_nueva = "null"):
        if pelicula_nueva == "null":
            pelicula_nueva = input ("ingrese el nombre de la pelicula a verificar: ").capitalize()

        for Pelicula in lista_peliculas:
            if pelicula_nueva == Pelicula.nombre:
                print ("Esa pelicula ya se encuentra en la lista")
                return False
        print ("esta pelicula no existe")
        return True

    def crear_pelicula(self):
        while True: #nombre:
            pelicula_nueva = input("ingrese el nombre de la pelicula: ").capitalize()
            if (self.verificar_pelicula(pelicula_nueva)): #verifica que no existe 
                break


        while True: #genero
            global generos
            print(f"\tLista de generos validos: ")
            for i in generos:
                print (i,end= " - ") 
            print(f"\t")
            genero_nuevo = input ("ingrese el genero de la pelicula: ")
            if genero_nuevo in generos:
                break
            else:
                print ("la pelicula no pertenece a un genero valido")


        while True: #pido ano
            try:
                ano_nuevo = int (input("ingrese el anio de la pelicula: "))
                break
            except:
                print("error en el ano")
        
        while True: #pido y chequeo la puntuacion
            try:
                puntuacion_nueva = float(input("ingrese la puntuacion de la pelicula: "))
                if puntuacion_nueva >0 and puntuacion_nueva <= 10:
                    break
                else:
                    print("error en puntuacion, debe ser mayor a 0 y hasta 10 puntos")
            except:
                print("error, la puntuacion debe ser numerica")
    
        nacionalidad_nueva = input ("ingrese la nacionalidad de la pelicula: ") #nacionalidad

        pelicula_nueva = cp.Pelicula (pelicula_nueva,genero_nuevo,ano_nuevo,puntuacion_nueva,nacionalidad_nueva)
        lista_peliculas.append(pelicula_nueva)
        pelicula_nueva.presentar()


    def cambiar_genero (self):
        global generos
        while True:
            pelicula_a_cambiar = input ("ingrese el nombre de la pelicula a modificar: ").capitalize()
            if  not self.verificar_pelicula(pelicula_a_cambiar):
                break

        while True:
            genero_nuevo = input ("ingrese el nuevo genero: ")
            if genero_nuevo in generos:
                print ("se cambio genero")
                self.genero= genero_nuevo
                break
            else:
                print ("El genero no se encuentra en la lista: ")
                for i in generos:
                    print (i,end= " - ") 
                print(f"\t")

    def presentar (self):
        for pelicula in lista_peliculas:
            pelicula.presentar()



        












