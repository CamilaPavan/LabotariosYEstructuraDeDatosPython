"""
Metodo writer()
writer = csv.writer(csvfile, dialect='excel', **fmtparams)
El objeto writer contienen los siguientes métodos públicos.
csvwriter.writerow(row): Escribe el parámetro de fila en el objeto de archivo del escritor, 
    formateado de acuerdo con el dialecto actual
csvwriter.writerows(rows) Escribe todos los elementos en rows 
    (un iterable de objetos row como se describe anteriormente) al objeto de archivo del writer, formateados según el dialecto actual.

"""
import os
path = os.path.abspath(os.path.dirname(__file__))


import csv
base_nueva = [["Fruta","Cantidad","Origen"],
                ["Manzana","2","Argentina"],
                ["Pera","3","Brasil"],
                ["Naranja","4","Uruguay"],]
with open(path+"\\Base_test_w.csv" , 'w') as f:#a+
    writer = csv.writer(f,delimiter = ",")
    #writer.writerow(base_nueva)
    writer.writerows(base_nueva)