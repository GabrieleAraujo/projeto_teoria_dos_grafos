
import networkx as nx
import matplotlib.pyplot as plt

# leitura do novo arquivo gerado para ser lido pela API no NetworkX
nome_arquivo = 'Projeto_Grafos_GabrieleAraujo/grafo_adj.gexf'

# Ler o arquivo GEXF e criar o grafo
grafo = nx.read_gexf(nome_arquivo)

# Plotar o grafo
plt.figure(figsize=(8, 6))
nx.draw(grafo, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=16, font_color='darkred', arrowstyle='-|>', arrowsize=10)
plt.show()