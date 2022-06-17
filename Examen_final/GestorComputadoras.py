
 
import Computadora as cp

computadoras_a_arreglar = []
lista_tecnicos = [["Bill Gates","Elon Musk","Mark Zuckerberg"],[0,0,0]]

class GestorComputadoras():

    #3.Mostrar tecnicos
    def mostrar_tecnicos (self):
        print ("   TECNICO    -    CANT DE PCs asignadas")
        for  i  in  range (len(lista_tecnicos [ 0 ])):
            print( f" { lista_tecnicos [ 0 ][ i ] }    -         { lista_tecnicos [ 1 ][ i ] }" )


    def crear_computadoras(self):

        global computadoras_a_arreglar
        global lista_tecnicos

        #Eleccion del tipo de pc
        while True:
            condicion=input(
        """ ------ TIPOS DE COMPUTADORAS ------
        Por favor ingrese una opcion a computadora a reparar
                1. Escritorio
                2. Notebook
        Numero : """)
            if (condicion=="1"): 
                break
            elif (condicion=="2"):
                break
            else:
                print ("opcion incorrecta")


        #-> numero_pc:único 
        flag_agregar = True
        while True:
            try:
                nueva_pc = int(input("ingrese el numero de la pc: "))
                for Computadora in computadoras_a_arreglar: 
                    if nueva_pc == Computadora.num_pc: 
                        print ("Esa computadora ya se encuentra en la lista")
                        flag_agregar = False
                        break
                if flag_agregar==True :
                    break
            except:
                print ("Dato incorrecto, debe ser un numero")

        #-> descripcion_problema: no puede estar vacio
        while True:
            problema = input ("ingrese el problema que tiene la computadora: ")
            contador = 0
            for i in range (len(problema)):
                contador +=1

            if contador == 0:
                print ("error, debe colocar el problema")
            else :
                break

        #-> tecnico: - Seleccion Tecnico
        while True:
            self.mostrar_tecnicos ()
            tecnico = input ("ingrese el nombre del tecnico: ")
            if tecnico in lista_tecnicos[0]:
                lista_tecnicos[1][lista_tecnicos[0].index(tecnico)] +=1
                print ("TABLA ACTUALIZADA")
                self.mostrar_tecnicos()
                break
            else:
                print ("dicho tecnico no se encuentra en la lista")

        #Loogear instancia Notebook
        if (condicion=="2"):
            import os
            path = os.path.abspath(os.path.dirname(__file__))
            path_archivo = path+"\\Notebook_a_arreglar.txt"
            try:
                fichero = open(path_archivo, 'a+')
                fichero.write(f"ID: {nueva_pc}, problema: {problema}, Tecnico: {tecnico} \n")
                fichero.close()
            except:
                print("ERROR.")

        instancia = cp.Computadora(nueva_pc,problema,tecnico)
        computadoras_a_arreglar.append(instancia)

        

    #2.Listar computadoras

    def listar_computadoras (self):
        for i in computadoras_a_arreglar:
            i.mostrar_informacion()





