from numpy import loadtxt

path = r'Python\01 - Machine learning\asset\pima-indians-diabetes.csv'

datapath= open(path, 'r')
data = loadtxt(datapath, delimiter=",")

""" Forma dei dati righe e colonne """
print(data.shape)

""" prime 3 righe del file """
print(data[:3])
