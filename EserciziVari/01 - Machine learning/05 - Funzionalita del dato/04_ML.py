from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier

path = r'Python\01 - Machine learning\asset\pima-indians-diabetes.csv'

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(path, names=names)
array = dataframe.values

X = array[:,0:8]
Y = array[:,8]

model = ExtraTreesClassifier()
model.fit(X, Y)
print(model.feature_importances_)