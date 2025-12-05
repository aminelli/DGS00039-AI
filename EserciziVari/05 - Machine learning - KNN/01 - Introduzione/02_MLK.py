import numpy as np
import pandas as pd

path = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

data = pd.read_csv(path, names=headernames)
array = data.values
X = array[:,:2]
Y = array[:,2]
print(data.shape)

from sklearn.neighbors import KNeighborsRegressor
knnr = KNeighborsRegressor(n_neighbors=10)
knnr.fit(X, Y)

print ("The MSE is:",format(np.power(Y-knnr.predict(X),2).mean()))
