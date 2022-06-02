import Chofer as cho
import Auto as au
lista_choferes = []
lista_autos = []

class gestorTaxis:
    def verificar_dni(self,dni):
        if(dni.isdigit() and len(dni) == 8):
            return True
        else:
            return False
    #La Clase Chofer tiene los atributos (nombre, apellido, dni, fecha nacimiento, Residencia)
    def crear_instancia_chofer(self):
        while True:
            flag = True
            dni = input("ingrese el dni del chofer: ")
            
            for c in lista_choferes:
                if(dni == c.get_dni()):
                    flag = False

            if (self.verificar_dni(dni) and flag):
                break
            else:
                print("El dni son solo numeros y tienen q ser 8 o ya existe")
        
        nombre = input("ingrese el nombre del chofer: ").capitalize()
        apellido = input("ingrese el Apellido del chofer: ").capitalize()
        fecha_nacimiento = input("ingrese la fecha nacimiento del chofer: ")
        residencia = input("ingrese la residencia del chofer: ")

        lista_choferes.append(cho.Chofer(nombre, apellido, dni, fecha_nacimiento, residencia))
    #"(self,patente,modelo,anio,marca,dni_chofer):

    
    def crear_instancia_auto(self):
        if(len(lista_choferes)==0):
            print("Es necesario tener choferes!!!")
            return

        while True:
            patente = input("ingrese la patente: (3 o mas Letras y 3 numeros)")
            cont_let = 0
            cont_num = 0
            for i in patente:
                if i.isdigit():
                    cont_num+=1
                elif i.isalpha():
                    cont_let+=1
            if(cont_let>=3 and cont_num ==3):
                break
        
        modelo = input("ingrese el modelo del Auto: ")
        anio = input("ingrese el año del Auto: ")
        marca = input("ingrese la marca del Auto: ")
        self.imprimir_info_choferes()
        while True:
            dni_chofer = input("ingrese el dni del chofer: ")
            for c in lista_choferes:
                    if(dni_chofer == c.get_dni()):
                        lista_autos.append(au.Auto(patente,modelo,anio,marca,dni_chofer))
                        return


    def imprimir_info_choferes(self):
        for i in lista_choferes:
            i.imprimir_info()

    def imprimir_info_autos(self):
        for i in lista_autos:
            i.imprimir_info()
    
    def modificar_chofer_auto(self):
        self.imprimir_info_autos()
        flag = True
        while flag:
            patente = input("ingrese la patente del auto a modificar el chofer: ")
            for i in lista_autos:
                if(patente == i.get_patente()):
                    flag = False
        
        flag = True
        self.imprimir_info_choferes()
        while flag:
            chofer = input("ingrese el dni del chofer: ")
            if (self.verificar_dni(chofer)):
                for i in lista_choferes:
                    if(chofer == i.get_dni()):
                        flag = False
            else:
                print("error en el formato de dni")
        
        for i in lista_autos:
            if(patente == i.get_patente()):
                i.set_chofer(chofer)
                    
 

    def imprimir_lista(self):
        print(lista_choferes)