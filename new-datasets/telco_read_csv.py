import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('new-datasets/all_telco_sites_metro.csv')

print(len(df))
print(df.head())

plt.scatter(df['longitude'], df['latitude'])
plt.show()