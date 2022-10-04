import pandas as pd
import numpy as np

df_ifog = pd.read_csv('/Users/helberthborelli/Documents/ifogsim2/codes/clustering-fog-nodes/datasets/ifogsim/edgeResources-melbCBD.csv')
df = pd.read_csv('/Users/helberthborelli/Documents/ifogsim2/codes/clustering-fog-nodes/datasets/ifogsim/clustered-resources-125.csv')

# df1 = pd.DataFrame(df_ifog, columns=['ID', 'Latitude', 'Longitude', ])

print(df)
