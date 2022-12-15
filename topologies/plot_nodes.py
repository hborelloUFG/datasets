import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('datasets/topologies/nsfnet/nsfnet_edges.json')

print(len(df))
print(df.head(30))

# plt.scatter(df['longitude'], df['latitude'])
# plt.show()