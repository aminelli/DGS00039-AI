from pandas import read_csv

path = r"Python\01 - Machine learning\asset\iris.csv"
data = read_csv(path)

""" Forma dei dati righe e colonne """
print(data.shape)

""" Clssificazione del tipo del dato """
print(data.dtypes)
