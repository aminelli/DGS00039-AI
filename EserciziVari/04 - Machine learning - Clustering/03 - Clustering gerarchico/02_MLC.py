from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt
import pandas as pd
# matplotlib inline
import numpy as np
from pandas import read_csv

path = r"Python\04 - Machine learning - Clustering\asset\pima-indians-diabetes.csv"

headernames = ['preg', 'plas', 'pres', 'skin',
               'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=headernames)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]

print(data.shape)

print(data.head())

patient_data = data.iloc[:, 3:5].values
plt.figure(figsize=(10, 7))
plt.title("Patient Dendograms")
dend = shc.dendrogram(shc.linkage(data, method='ward'))

plt.show()

cluster = AgglomerativeClustering(
    n_clusters=4, affinity='euclidean', linkage='ward')
cluster.fit_predict(patient_data)
plt.figure(figsize=(10, 7))
plt.scatter(patient_data[:, 0], patient_data[:, 1], c=cluster.labels_, cmap='rainbow')

plt.show()
