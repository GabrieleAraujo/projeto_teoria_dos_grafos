# Imports
import numpy as np
import networkx as nx  #pip install networkx

class Grafo:
    def __init__(self, path):
        self.matriz_adj, self.vertices, self.indice_vertices, self.dirigido = self.ler_arquivo(path)
        
    # Entrada de arquivo e armazenamento na estrutura de dados
    def ler_arquivo(self, path):
        with open(path, 'r') as arquivo:
            dirigido = arquivo.readline().strip()  # "D" ou "ND"
            arestas = [line.strip().split(',') for line in arquivo.readlines()] # vírgula
            arestas = [[v.strip() for v in aresta] for aresta in arestas]  # espaços em branco dos vértices

        # extrair os vértices únicos e ordená-los
        vertices = set(sum(arestas, []))
        vertices = sorted(vertices)
        indice_vertices = {v: i for i, v in enumerate(vertices)}

        # Matriz de adjacência
        n = len(vertices)
        matriz_adj = np.zeros((n, n), dtype=int)
        for v1, v2 in arestas:
            matriz_adj[indice_vertices[v1]][indice_vertices[v2]] = 1
            if dirigido == 'ND':
                matriz_adj[indice_vertices[v2]][indice_vertices[v1]] = 1

        return matriz_adj, vertices, indice_vertices, dirigido == 'D'



    # Apresentar se dois vértices vX e vY são ou não adjacente
    def sao_adjacentes(self, v1, v2):
        return self.matriz_adj[self.indice_vertices[v1]][self.indice_vertices[v2]] != 0
    def verificar_adjacencia(self):
        while True:
            entrada = input("Digite dois vértices separados por espaço para verificar adjacência (ou 'sair' para terminar): ")
            if entrada.lower() == 'sair':
                break
            v1, v2 = entrada.split()
            if v1 in self.indice_vertices and v2 in self.indice_vertices:
                adjacente = self.sao_adjacentes(v1, v2)
                print(f"Os vértices {v1} e {v2} são{' ' if adjacente else ' não '}adjacentes.")
            else:
                print("Um ou ambos os vértices não foram encontrados. Tente novamente.")

    # Calcular o grau de um vértice qualquer
    def grau_do_vertice(self, v):
        return np.sum(self.matriz_adj[self.indice_vertices[v]])
    def verificar_grau(self):
        while True:
            entrada = input("Digite o vértice para verificar o seu grau (ou 'sair' para terminar): ")
            if entrada.lower() == 'sair':
                break
            if entrada in self.indice_vertices:
                grau = self.grau_do_vertice(entrada)
                print(f"O vértice {entrada} possui {grau} graus.")
            else:
                print("Vértice não encontrado. Tente novamente.")    



    # Buscar todos os vizinhos de vértice qualquer
    def vizinhos_do_vertice(self, v):
        idx = self.indice_vertices[v]
        return [self.vertices[i] for i, adj in enumerate(self.matriz_adj[idx]) if adj != 0]
    def verificar_vizinhos(self):
        while True:
            entrada = input("Digite um vértice para verificar seus vizinhos (ou 'sair' para terminar): ")
            if entrada.lower() == 'sair':
                break
            v1 = entrada.strip()
            if v1 in self.indice_vertices:
                vizinhos = self.vizinhos_do_vertice(v1)
                if vizinhos:
                    print(f"Os vizinhos do vértice {v1} são: {', '.join(vizinhos)}.")
                else:
                    print(f"O vértice {v1} não possui vizinhos.")
            else:
                print("Vértice não encontrado. Tente novamente.")

    # Visitar todas as arestas do grafo
    def visitar_arestas(self):
        arestas = set()
        for i, v1 in enumerate(self.vertices):
            for j, v2 in enumerate(self.vertices):
                if self.matriz_adj[i][j] != 0:
                    if self.dirigido:
                        arestas.add((v1, v2))  # Mantém a direção das arestas para grafos dirigidos
                    else:
                        # Adiciona a aresta garantindo que a ordem dos vértices não importe
                        arestas.add(tuple(sorted((v1, v2))))
        return list(arestas)  # Converte o conjunto para lista antes de retornar

    def gerar_novo_arquivo(self, filename='Projeto_Grafos_GabrieleAraujo/data/grafo_adj.gexf'):
        G = nx.DiGraph() if self.dirigido else nx.Graph()
        for vertice in self.vertices:
            G.add_node(vertice)
        for i in range(len(self.matriz_adj)):
            for j in range(len(self.matriz_adj[i])):
                if self.matriz_adj[i][j] == 1:
                    G.add_edge(self.vertices[i], self.vertices[j])

        nx.write_gexf(G, filename)
        return G
