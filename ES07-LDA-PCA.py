from sklearn.datasets import load_iris
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn import decomposition

X, y = make_classification(
    n_samples=1000,
    n_features=4,
    n_informative=2, 
    n_redundant=0,
    random_state=0, 
    shuffle=False
)
 
print(X)
 
 
clf = LinearDiscriminantAnalysis()
clf.fit(X,y)

p = clf.predict([[4,3,0.5,1]])
 
print(p)


clf = PCA()

clf.fit(X,y)

print(clf.explained_variance_ratio_)
print(clf.singular_values_)


iris =load_iris()
X = iris.data
y = iris.target

f = plt.figure(1)
plt.scatter(X[:,0],X[:,1], c= y)

plt.xlabel("sepals length")
plt.ylabel("sepals width")
plt.title("Dati")
f.show()

# Perform PCA
pca = decomposition.PCA(n_components=3)

pca.fit(X)
X1 = pca.transform(X)

# Plot
g = plt.figure(2)
#y = np.choose(y, X1[:, 1], c=y)

plt.scatter(X1[:, 0], X1[:, 1], c=y)

plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title("PCA Data")
g.show()

print("")



 
 