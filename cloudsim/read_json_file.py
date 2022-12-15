import pandas as pd

df = pd.read_json('cloudsim/json/nodes.json')

print(df)

print(len(df))