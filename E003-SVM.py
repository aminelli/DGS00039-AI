import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, MinMaxScaler


# Caricamento del dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print("=======================================")
print("Righe Originarie:")
print("")
print(df.head(),"\n")
print("=======================================")

print("")
print("")

# Standardizzazione (media = 0, var = 1)
std_scaler = StandardScaler()
df_std = pd.DataFrame(std_scaler.fit_transform(df), columns=df.columns)
print("=======================================")
print("Righe Standardizzate:")
print("")
print(df_std.head, "\n")
print("=======================================")

print("")
print("")

# Normalizzazione (min-max[0,1])
mm_scaler = MinMaxScaler()
df_mm = pd.DataFrame(mm_scaler.fit_transform(df), columns=df.columns)
print("=======================================")
print("Normalizzazione (min-max[0,1]):")
print("")
print(df_mm.head, "\n")
print("=======================================")

print("")
print("")
print("")
print("")

# Confronto statistico

print("=======================================")
print("Statistiche Originali:")
print("")
print(df.describe(), "\n")
print("=======================================")

print("")
print("")

print("=======================================")
print("Statistiche dopo Standardizzazione:")
print("")
print(df_std.describe(), "\n")
print("=======================================")

print("")
print("")

print("=======================================")
print("Statistiche dopo Normalizzazione:")
print("")
print(df_mm.describe(), "\n")
print("=======================================")

print("")
print("")