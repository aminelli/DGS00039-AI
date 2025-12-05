import csv
import numpy as np

path = "/Users/tony/Desktop/CORSI/IA/Python.Code/Codice lezione/01 - Machine learning/01 - Caricamento dei Dati/asset/iris.csv"

with open(path,'r') as f:
   reader = csv.reader(f,delimiter = ',')
   headers = next(reader)
   data = list(reader)
   data = np.array(data).astype(np.string_)

""" Intestazioni del file """
print(headers)

""" Forma dei dati righe e colonne """
print(data.shape)

""" prime 3 righe del file """
print(data[:3])
