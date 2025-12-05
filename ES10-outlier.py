import pandas as pd

df = pd.DataFrame({
    "values" : [10,12,11,14,13,12,11,999,10,13,12,15] # 999 è outlier
})

# Calcolo IQR

Q1 = df["values"].quantile(0.25)
Q3 = df["values"].quantile(0.75)
IQR = Q3 - Q1

low_limit = Q1 - 1.5 * IQR
high_limit = Q3 + 1.5 * IQR

df_filter = df[
    (df["values"] >= low_limit) & (df["values"] <= high_limit)
]

print("Originale:\n", df)
print("Filtrato:\n", df_filter)
