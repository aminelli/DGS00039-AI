from sklearn import svm, datasets
import pandas as pd
from matplotlib import pyplot
from pandas.plotting import scatter_matrix


df = pd.read_csv('./datasets/iris.csv')

print (df.shape)
print (df.head(10))
print (df.tail(9))
print (df.describe())


# Conteggio dei NAN
print(df.isna().sum().sum())

# Eliminazione righe con valori mancanti che
# potrebbero ingannare l'algoritmo
df = df.dropna()

print(df.groupby('species').size())

# istogramma
df.hist()
pyplot.show()
# Scatter plot matrix
scatter_matrix(df)
pyplot.show()

X = df.values[:, :2]
s = df['species']
d = dict([(y, x) for x,y in enumerate(sorted(set(s)))])
y = [d[x] for x in s]

clf = svm.SVC()

clf.fit(X,y)

# Predizione

p = clf.predict([[5.4, 3.3]])

print(p)

print("")



