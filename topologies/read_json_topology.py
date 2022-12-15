import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# from networkx.drawing.nx_pydot import graphviz_layout

data = 'nsfnet'
# data = 'geant2'
# data = 'germany'

df_edges = pd.read_json('datasets/topologies/'+data+'/'+data+'_edges.json')
# print(df_edges)

G = nx.from_pandas_edgelist(df_edges, 'source', 'target')

print(df_edges)
print('bandwidth:', df_edges['bandwidth'].unique())
print('weight:', df_edges['weight'].unique())

print(G.nodes)

# size = 0
for d in G.degree():
    if d[1]==5:
        print(d)

node = 34
# imprimindo links do nó especificado
 
nx.draw(G, with_labels=True)
plt.show()
# pos = nx.nx_agraph.graphviz_layout(G, prog="twopi")
# nx.draw(G, pos)
# plt.show()