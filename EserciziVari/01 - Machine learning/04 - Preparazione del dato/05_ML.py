from sklearn.preprocessing import StandardScaler
from pandas import read_csv
from numpy import set_printoptions

path = r'Python\01 - Machine learning\asset\pima-indians-diabetes.csv'

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(path, names=names)
array = dataframe.values

data_scaler = StandardScaler().fit(array)
data_rescaled = data_scaler.transform(array)

set_printoptions(precision=2)
print ("\nRescaled data:\n", data_rescaled [0:5])
