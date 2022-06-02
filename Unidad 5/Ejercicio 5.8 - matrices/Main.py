"""
## Ejercicio 5.8 (Programa de ventas)
El programa debe:
* Simular un programa que venda 3 productos
Codigo Nombre Precio Stock
    1 y producto1 y 300 y 5
    2 y producto2 y 400 y 4
    3 y producto3 y 500 y 7
* El menú debe mostrar los productos a comprar. -> LISTO
* Luego se debe contar con un menu de si se pagara en efectivo o tarjeta credito o debito -> LISTO
* Contar con 7 funciones disponibles en el menú:
  1. Ver menú de productos (Formato: codigo - producto) -> LISTO
  2. Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock) -> LISTO
  3. Pagar con tarjeta debito (se debe descontar el stock) -> LISTO
  4. Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock) -> LISTO
  5. Consultar productos y stock -> LISTO
  6. Agregar stock a los productos
  7. Cambiar el precio a los productos
  
* Gestionar posibles errores
* Estructurar el programa a criterio propio
"""


import funciones_imprimir as fi
import variables as vr




def forma_de_pago(): #se pide forma de pago y te deja comprar 
  while True:
    forma_pago= input("""ingrese la forma de pago
                      1. CREDITO
                      2. DEBITO
                      3. EFECTIVO
                      Opcion: """)
    if forma_pago == "1":
      producto = producto_que_desea_comprar()
      if producto == "producto1":
          if(vr.base_productos[3][0]>0):
            vr.base_productos[3][0] =vr.base_productos[3][0]-1 #resto stock
            print(f"El comprador debe pagar: {vr.base_productos[2][0]*1.1}")
            return
          else:
            print ("producto sin stock")
      elif producto == "producto2":
          if(vr.base_productos[3][1]>0):
            vr.base_productos[3][1] =vr.base_productos[3][1]-1 #resto stock
            print(f"El comprador debe pagar: {vr.base_productos[2][1]*1.1}")
            return
          else:
            print ("producto sin stock")
      elif producto == "producto3":
            if(vr.base_productos[3][2]>0):
              vr.base_productos[3][2] =vr.base_productos[3][2]-1 #resto stock
              print(f"El comprador debe pagar: {vr.base_productos[2][2]*1.1}")
              return
            else:
              print ("producto sin stock")
      else:
        print ("Error")

    elif forma_pago == "2":
      producto = producto_que_desea_comprar()
      if producto == "producto1":
          if(vr.base_productos[3][0]>0):
            vr.base_productos[3][0] =vr.base_productos[3][0]-1 #resto stock
            print(f"El comprador debe pagar: {vr.base_productos[2][0]}")
            return
          else:
            print ("producto sin stock")
      elif producto == "producto2":
          if(vr.base_productos[3][1]>0):
            vr.base_productos[3][1] =vr.base_productos[3][1]-1 #resto stock
            print(f"El comprador debe pagar: {vr.base_productos[2][1]}")
            return
          else:
            print ("producto sin stock")
      elif producto == "producto3":
            if(vr.base_productos[3][2]>0):
              vr.base_productos[3][2] =vr.base_productos[3][2]-1 #resto stock
              print(f"El comprador debe pagar: {vr.base_productos[2][2]}")
              return
            else:
              print ("producto sin stock")
      else:
        print ("Error")
      
    elif forma_pago == "3":
      producto = producto_que_desea_comprar()
      if producto == "producto1":
          if(vr.base_productos[3][0]>0):
            vr.base_productos[3][0] =vr.base_productos[3][0]-1 #resto stock
            print(f"El comprador debe pagar: {vr.base_productos[2][0]}")
            return
          else:
            print ("producto sin stock")
      elif producto == "producto2":
          if(vr.base_productos[3][1]>0):
            vr.base_productos[3][1] =vr.base_productos[3][1]-1 #resto stock
            print(f"El comprador debe pagar: {vr.base_productos[2][1]}")
            return
          else:
            print ("producto sin stock")
      elif producto == "producto3":
            if(vr.base_productos[3][2]>0):
              vr.base_productos[3][2] =vr.base_productos[3][2]-1 #resto stock
              print(f"El comprador debe pagar: {vr.base_productos[2][2]}")
              return
            else:
              print ("producto sin stock")
      else:
        print ("Error")

    else:
      print ("Error en forma de pago")



def producto_que_desea_comprar():
    while True:
      producto_a_comprar= input("""ingrese que producto desea comprar
                        1. producto 1
                        2. producto 2
                        3. producto 3
                        Opcion: """)
      if producto_a_comprar == "1":
        return "producto1"
      elif producto_a_comprar == "2":
        return "producto2"
      elif producto_a_comprar == "3":
        return "producto3"
      else:
        print ("ninguna opcion es correcta")


forma_de_pago()








#fim.imprimir_matriz2(base_productos)
