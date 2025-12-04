from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
import pandas as pd


cancer = load_breast_cancer()
print(cancer['feature_names'])
print(cancer['data'])
print(cancer.target_names)

# Tutti i dati
X = cancer.data

# Classi
y = cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

clf = SVC()

clf.fit(X_train, y_train)

# Prediction
y_predict = clf.predict(X_test)

# Stampa matrice di confusione
cm = np.array(confusion_matrix(y_test, y_predict, labels=[1, 0]))

confusion = pd.DataFrame(
    cm,
    index=['is_cancer', 'is_healthy'],
    columns=['predict_cancer','predict_healthy']
)

print("=====================================")
print("confusion")
print(confusion)


print("=====================================")
print("classificatio")
+print(classification_report(y_test, y_predict))

