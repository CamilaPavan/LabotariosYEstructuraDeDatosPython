"""
El programa debe:

Pedir al usuario un número entero positivo y mostrar por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
while True:
    try:
        valor = int (input("por favor ingrese el valor "))
        if valor <= 0:
            print ('el valor debe ser positivo')
            continue
        break
    except:
        print ("ingrese nuevamente un valor valido")

for i in range (valor,-1,-1):
    if i == 0: # para que no imprima la ultima coma. 
        print (i)
    else:
        print(i,end= ",")