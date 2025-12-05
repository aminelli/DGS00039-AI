from pandas import read_csv

path = r'Python\01 - Machine learning\asset\pima-indians-diabetes.csv'

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=names)
count_class = data.groupby('class').size()

""" Stampa la distribuzione delle classi """
print(count_class)
