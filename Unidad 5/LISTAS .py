"""
Listas
Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. Son:

    Ordenadas: mantienen el orden en el que han sido definidas.
    mutables: pueden cambiar el contenido.
    dinámicas: modificar el número de elementos que contiene (añadir o eliminar elementos).
Pueden ser formadas por tipos arbitrarios

Pueden ser indexadas con [i].

Se pueden anidar, es decir, meter una dentro de la otra. .

Una lista sea crea con [ ] separando sus elementos con comas
"""



lista = [1,2,3,"fede",True] #podemos ponerle cualquier valor. 

print(lista[3])
print(lista[-1]) #El -1 imprime el ultimo valor de la lista. 

print(lista[0:2]) #Aca va a llamar al 1 y el 2 , porque el 3 que esta en
#la posiicion 2 no lo toma, siempre es a menos 1 

lista = [1, 2, 3, "hola", "chau"]
for i in lista: #iteramos la lista. 
    print(i)

lista = [1,2,3]
print(len(lista))
def fun():
  global lista
  for i in range(len(lista)): #otra forma de iterar. 
      print(lista[i])
fun()

cadena = "Hola como estas" #podes cambiar la frase a cada letra un elemnto de la lista
lista = list(cadena) #tengo que poner la funcion "list(var1)" , y al tengo que guardar en una variable. 
print(lista)
#los NUMEROS ENTEROS NO SE PUEDEN CONVERTIR EN LISTA, PRIMERO HAY QUE CASTEARLOS. 


cadena="Hola este es el split"
lista=cadena.split() #separa en elementos por los espacios, es decir en cada palabra. 
print(lista)



lista = [6,2,1,98,2]
lista.append(8) #agregar un elemento
lista.sort() #ordenar de menor a mayor 
print(lista)
lista.sort(reverse= True) #de mayor a menor
print (lista)

lista_max = [1,2,5,4,10,28,6]
print(max(lista_max))  #imprimir el mas grande la lista 