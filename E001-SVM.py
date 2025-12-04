# pip install scikit-learn
from sklearn import svm

# [Altezza, Peso, Nr Scarpe]
X = [ 
     [170, 70, 42],
     [180, 80, 44],
     [170, 65, 38],
     [165, 55, 36],
     [168, 62, 37],
]

# Classi Generi U = Uomo = 0 e D = Donna = 1

y = [0, 0, 0, 1, 1] 

clf = svm.SVC();
clf.fit(X, y)

# Predizione

p = clf.predict([[178, 85, 44]])

print(p)

