from pandas import read_csv

path = r'Python\01 - Machine learning\asset\pima-indians-diabetes.csv'

headernames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=headernames)

""" prime 10 righe del file """
print(data.head(10))
