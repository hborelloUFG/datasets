import numpy as np
import pandas as pd

# print('lendo arquivo csv...')
df = pd.read_csv('~/Documents/ifogsim2-notes/codes/datasets/1000-nodes.csv')

# df = pd.read_csv('~/Documents/ifogsim2-notes/codes/datasets/Tuple100K.csv')

# print(df)

print('max mips:', df['MIPS'].max(), '| max ram', df['RAM'].max(), '| max bw:', df['BW'].max())
print('max mips:', df['MIPS'].min(), '| max ram', df['RAM'].min(), '| max bw:', df['BW'].min())