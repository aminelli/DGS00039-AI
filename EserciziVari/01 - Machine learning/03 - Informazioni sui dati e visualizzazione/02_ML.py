from matplotlib import pyplot
from pandas import read_csv

path = r'Python\01 - Machine learning\asset\pima-indians-diabetes.csv'

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=names)
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)

pyplot.show()
