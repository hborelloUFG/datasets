from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df_melb = pd.read_csv('../datasets/ifogsim/edgeResources-melbCBD.csv')

df_qcy = pd.read_csv('../datasets/qws/qws2.csv')

qcy = len(df_qcy)
print(qcy)
# print(df_melb)

min_lat = df_melb['Latitude'].min()
max_lat = df_melb['Latitude'].max()
min_lon = df_melb['Longitude'].min()
max_lon = df_melb['Longitude'].max()


ran_lat = np.random.uniform(low=min_lat, high=max_lat, size=qcy)
ran_lon = np.random.uniform(low=min_lon, high=max_lon, size=qcy)

df = pd.DataFrame({'Longitude': ran_lon, 'Latitude': ran_lat, 'Latency': df_qcy['latency']})
print(df)

if True:
    X = pd.DataFrame(df, columns=['Latitude', 'Longitude']).to_numpy()

    f, axes = plt.subplots(figsize=(16,8))
    axes.set(xlabel='Longitude', ylabel='Latitude', title='Fog Nodes (Melbourne CBD)')
    axes.scatter(X[:,1], X[:,0])

    plt.show()
else:
    df.to_csv('results/fog-resources-2500.csv', index=False)