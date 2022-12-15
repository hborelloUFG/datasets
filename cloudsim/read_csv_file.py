import pandas as pd


df_1 = pd.read_csv('cloudsim/csv/table1.csv', delimiter=';')
df_2 = pd.read_csv('cloudsim/csv/table1.csv', delimiter=';')

print(df_1.head())
print(len(df_1))

print(df_2.head())
print(len(df_2))