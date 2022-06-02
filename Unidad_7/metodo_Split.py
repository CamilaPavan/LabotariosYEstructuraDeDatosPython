#De una cadena devuelve una lista, con elementos "cortados" en donde indiquemos 
mail = 'fede@gmail.com'
mail.split('@')
lista = "fede,hola,chau"
lista_1 = lista.split(',')#separa en las comas
print(lista_1)
lista2= "me llamo cami"
lista_2 = lista2.split() #separa por los espacios
print (lista_2)


#corto en el @ e imprimo la pos 0 de la lista
mail = 'federico@gmail.com'
usuario = mail.split('@')[0]
print(f'El usuario es {usuario}.')

#Separa palabras
cadena = 'El otro día fui al supermercado y compré un Baggio de Manzana'
palabras = cadena.split()
print(palabras)