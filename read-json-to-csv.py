import pandas as pd

df = pd.read_json('/Users/borelli/Documents/ifogsim2-notes/codes/clustering-fog-nodes/datasets/appication-config.json')


df_res = pd.DataFrame(df, columns=['appId', 'userId', 'cpu_c_m1', 'cpu_m1_m3', 'cpu_m1_m2', 'nw_m1_m2', 
                                    'nw_c_m1', 'nw_m1_m3', 'nwLength', 'mService2', 'client', 
                                    'mService3', 'throughput', 'mService1'])


# df.to_csv('/Users/borelli/Documents/ifogsim2-notes/codes/clustering-fog-nodes/datasets/appication-config.csv', float_format='%.2f', index=False)


print(df_res)