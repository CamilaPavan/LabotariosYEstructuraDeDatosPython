"""
Los diccionarios en Python son una estructura de datos que permite almacenar su contenido en forma de llave (key) y valor.
A diferencia de las listas, que se indexan mediante un rango numérico, 
los diccionarios se indexan con llave, que pueden ser cualquier tipo inmutable (no se cambia); las cadenas y números siempre pueden ser claves.
Algunas propiedades:

Son dinámicos, pueden crecer o decrecer, se pueden añadir o eliminar elementos.
Son indexados, los elementos del diccionario son accesibles a través del key.
Son anidados, un diccionario puede contener a otro diccionario en su campo value.
Entonces:

Es una colección de elementos, donde cada uno tiene una llave key y un valor value.
Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value.

"""



#RECOMENDADO
diccionario_persona = {
    "Nombre": "juan",
    "Edad": 30,
    "DNI": 12345678
}
#lo primero es la llave, en este caso "nombre", "edad" y "DNI". y lo segundo el valor que conitiene. 
# KEY = como vas a buscar el valor, 

#ITERAR EL DICCIONARIO, osea recorrerlo. 
diccionario_persona = {
    "Nombre": "juan",
    "Edad": 30,
    "DNI": [1,2,3,4,5]
}
nombre = "Nombre"
print(diccionario_persona[nombre]) #solo imprimir el valor de esa KEY

#imprime los key, entras
print("---------------Keys---------------")
for i in diccionario_persona:
  print(i)


print("---------------Valores---------------")
#imprime los valores
for i in diccionario_persona:
  print(diccionario_persona[i]) #este valor i, imprime los valores

#iterar key y valor juntos, como listas 
print(diccionario_persona.items())
#Mas prolijo 
for i, j in diccionario_persona.items():
    print(f"Key: {i} - Valor: {j}")

#-------  -------

diccionario_persona = {
    "Nombre": "juan",
    "Edad": 30,
    "DNI": [1,2,3,4,5],
}

print(diccionario_persona)
diccionario_persona.update({"Nombre":"Federico"})
print(diccionario_persona)

print(diccionario_persona)
print(diccionario_persona.get("Nombrea","No existe")) #Si existe la key, me retorna el valor. Si no existe me retorna lo que pongo despues de la coma.
#para agregar el valor 
diccionario_persona.update({"Nombre4":"Federico"}) #inserta un nuevo key, o actualiza su valor si ya existe. 
print(diccionario_persona)


print (diccionario_persona)
diccionario_persona.pop("Nombre") #Elimina la key y su valor 
print (diccionario_persona)

print("---------------")
print(type(diccionario_persona))


#print(diccionario_persona.get("DNI","No existe")[2])


