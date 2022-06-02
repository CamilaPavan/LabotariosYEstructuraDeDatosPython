"""
cuando ponemos una lista adentro de otra estamos hablando de una mtriz
"""


Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[10,30,50]]
print(Taxis)
print(len(Taxis))

for i in range(len(Taxis)):
  print(f"{Taxis[0][i]} - {Taxis[1][i]} - {Taxis[2][i]}") #asi recorro los valores de cada lista 

def matriz_nula(filas, columnas): #crear una matriz nula, solo ejemplo, no lo usamos 
  matriz = []
  for i in range(filas):
    matriz.append( [0] * columnas )
  return matriz

print(matriz_nula(2,3))