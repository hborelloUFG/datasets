import pandas as pd
import numpy as np

# https://qwsdata.github.io/
#   0            1              2               3               4           5           6               7           8           9          10    
# response.time, availability, throughput, successability, reliability, compliance, best.practices, latency, documentation, service.name, wsdl.address
df_full = pd.read_csv('qws/txt/qws2.txt')
df_full=df_full.drop(columns=['10', '11'])

df_full.rename(columns={'0':'response.time','1':'availability','2':'throughput',
                        '3':'successability','4':'reliability','5':'compliance',
                        '6':'best.practices','7':'latency','8':'documentation',
                        '9':'service.name'}, inplace = True)

print(df_full.head())

print('nr de registros:', len(df_full))

# df_full.to_csv('~/Documents/ifogsim2-notes/codes/clustering-fog-nodes/datasets/qws/qws2.csv', index=False)


X = pd.DataFrame(df_full, columns=['response.time','throughput', 'latency']).to_numpy()


# https://www.ehow.com.br/calcular-mips-como_73799/
X[:,0] = X[:,0]/1000
Y = X[:,1]/X[:,0]

X = np.insert(X, 2, Y, axis=1)

df_mips = pd.DataFrame(X, columns=['response.time.s', 'throughput', 'latency', 'mips'])

df_mips['throughput'] = df_mips['throughput'].apply(np.ceil)
df_mips['mips'] = df_mips['mips'].round(decimals=2)

print(df_mips)

# df_mips.to_csv('~/Documents/ifogsim2-notes/codes/clustering-fog-nodes/datasets/qws/qws2-mips.csv', index=False, float_format='%.2f')

# for i in range(len(X)):
#     print(i, X[i,11])

# print(X[1799,10])
