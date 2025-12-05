from pandas import read_csv
from scipy.stats import uniform
from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV

path = r"Python\05 - Machine learning - KNN\asset\pima-indians-diabetes.csv"

headernames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=headernames)
array = data.values
X = array[:,0:8]
Y = array[:,8]

param_grid = {'alpha': uniform()}
model = Ridge()
random_search = RandomizedSearchCV(estimator=model, param_distributions=param_grid, n_iter=50,
random_state=7)
random_search.fit(X, Y)

print(random_search.best_score_)
print(random_search.best_estimator_.alpha)
