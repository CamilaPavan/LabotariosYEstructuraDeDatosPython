base_datos_artuculos= {}

class GestorMain():
    def crear_articulo(self):

        tipo_producto = input ("Ingrese el tipo de producto: ").capitalize()
        print ("DETALLES DEL ARTICULO")
        nacionalidad = input("Ingrese la nacionalidad del articulo: ")
        color = input ("Ingrese el color del articulo: ")
        categoria = input("Ingrese el tipo de categoria: Ninos , bebes o Adultos: ") #A este despues hacele los chequeos para que ingrese eso o de error.

        #Borra estos comentarios.
        #Aca agrega cualquier detalle, incluso proba con eso de que las personas ingresen las cateregorias si queres.

        dic_detalles = {
            "Nacionalidad" : nacionalidad,
            "color": color,
            "Categoria": categoria
        }

        dic_articulo = {
            "Tipo": tipo_producto,
            "detalle": dic_detalles #Agrego un diccionario dentro de otro para darle los dos niveles
        }

        #se crea una variable, para darle al articulo ese valor
        nombre_del_articulo = tipo_producto 
        base_datos_artuculos.update({nombre_del_articulo: dic_articulo})

        print (base_datos_artuculos)

    def agregar_atributo_a_articulo(self): #La de borrar es lo mismo, pero lo pones "pop" en vez de update
        while True: 
            #muestros los articulos guardados.
            for i,j in base_datos_artuculos.items():
                print (f"Articulo: {i}")
            
            articulo_a_agregar = input("A que articulo desea agregarle detalle: ").capitalize()
            for i,j in base_datos_artuculos.items():
                if articulo_a_agregar == i:
                    key_nuevo_detalle = input(f"Ingrese el nombre del detalle que desea a agregarle a {i}: ")
                    valor_nuevo_detalle = input(f"Que valor desea agregarle a {key_nuevo_detalle}: ")
                    j.update({key_nuevo_detalle:valor_nuevo_detalle})
                    return
                else:
                    print ("No se encuentra ese articulo")

    def mostrar_articulos(self):
        for i, j in base_datos_artuculos.items():
            print(f"Key: {i} - Valor: {j}")




   
gestor = GestorMain()

while True:
    opcion = input ("""
    --- MENU ---
    1. Crear articlo
    2. agregar mas detalle al articulo
    3. x
    4. x
    5. Mostrar articulos
    6. Salir
    Opcion: """)
    if opcion == "1":
        gestor.crear_articulo()
    elif opcion == "2":
        gestor.agregar_atributo_a_articulo()
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        gestor.mostrar_articulos()
    elif opcion == "6":
        break
    else:
        print("Error, valor no valido.")


