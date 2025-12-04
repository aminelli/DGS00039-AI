from sklearn import svm, datasets

iris = datasets.load_iris()

print(iris.data)

X = iris.data[: , :2]

# 0: setosa, 1: Versicolor 2_ Virginica
y = iris.target

print(y)

clf = svm.SVC();
clf.fit(X, y)

# Predizione

p = clf.predict([[5.4, 3.3]])

print(p)
print("END")
