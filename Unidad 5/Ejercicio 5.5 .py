"""
Tener el abecedario en la una lista
pedir a usuario un numero(solo 2 o 3)
Elimina de la lista las letras que ocupan los posiciones
de multiplos de esa lista. (posisicion literal)
mostrar por pantalla las letras resultantes. 
"""
def abecedario():
    abecedario= ("abcdefghijklmnñopqrstuvwxyz")
    abecesario_en_lista = list (abecedario)
    while True:
        try: 
            valor=int(input("por favor coloque el valor 2 o 3: "))
            if valor == 2 or valor == 3:
                break
        except:
            print ("por favor coloque 1 o 2")
    if valor == 2:
        posicion = 0
        for i in abecesario_en_lista:
            posicion+=1
            if posicion % valor == 0:
                abecesario_en_lista.remove(i)
            else:
                pass
        print (abecesario_en_lista)
    elif valor == 3:
        posicion = 0
        for i in abecesario_en_lista:
            posicion += 1
            if posicion % valor == 0:
                abecesario_en_lista.remove(i)
            else:
                pass
        print (abecesario_en_lista)
                


abecedario()