from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import Normalizer

path = r'Python\01 - Machine learning\asset\pima-indians-diabetes.csv'

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv (path, names=names)
array = dataframe.values

Data_normalizer = Normalizer(norm='l1').fit(array)
Data_normalized = Data_normalizer.transform(array)

set_printoptions(precision=2)
print ("\nNormalized data:\n", Data_normalized [0:3])
