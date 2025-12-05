from pandas import read_csv
from pandas import set_option

path = r'Python\01 - Machine learning\asset\pima-indians-diabetes.csv'

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=names)
set_option('display.width', 100)
set_option('precision', 2)

""" Forma dei dati righe e colonne """
print(data.shape)

""" Stampa le proprietà statistiche dei dati """
print(data.describe())
