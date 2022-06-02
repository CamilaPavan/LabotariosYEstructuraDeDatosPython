"""
Metodo Reader()
reader = csv.reader(csvfile, dialect='excel', **fmtparams)
Retorna un objeto reader que iterará sobre las líneas del csvfile proporcionado
"""


import os
path = os.path.abspath(os.path.dirname(__file__))
import csv

with open(path+"\\base_test.csv") as f:
    reader = csv.reader(f,delimiter = ",") #csv.reader(f,delimiter = ";")
    for fila in reader:
        #print(fila)
        print(f"{fila[0]} - {fila[1]} - {fila[2]}")
