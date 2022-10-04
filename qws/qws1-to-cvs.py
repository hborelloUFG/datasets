import pandas as pd
import numpy as np

#   0            1              2               3               4           5           6               7           8       9       10      11          12
# response.time, availability, throughput, successability, reliability, compliance, best.practices, latency, documentation, wsrf, class, service.name, wsdl.address

df_full = pd.read_csv('~/Documents/ifogsim2-notes/codes/clustering-fog-nodes/datasets/qws/txt/qws1.txt')
df = pd.DataFrame(df_full, columns=['0','1','2','3','4', '5', '7', '11'])

print(df.head())

print('nr de registros:', len(df))

