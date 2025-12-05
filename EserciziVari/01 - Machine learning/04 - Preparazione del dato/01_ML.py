from pandas import read_csv
from numpy import set_printoptions
from sklearn import preprocessing

path = r'Python\01 - Machine learning\asset\pima-indians-diabetes.csv'

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(path, names=names)
array = dataframe.values

data_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
data_rescaled = data_scaler.fit_transform(array)

set_printoptions(precision=1)
print ("\nScaled data:\n", data_rescaled[0:10])
