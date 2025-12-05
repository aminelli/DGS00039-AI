# NONN SUPERVISIONATO
from sklearn.cluster import KMeans

import numpy as np

X = np.array([
    [1,2,3],
    [1,4,2],
    [1,0,5],
    [10,2,4],
    [9,4,3],
    [11,0,2]
])


kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

print(kmeans.labels_)
print(kmeans.cluster_centers_)
print(kmeans.predict([[1,2,4]]))