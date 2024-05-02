
from Parte_1 import Grafo
from detect_ciclos import detectar_ciclos

def main():
    path = 'Projeto_Grafos_GabrieleAraujo/data/grafo.txt'
    grafo = Grafo(path)

    # print("Matriz de Adjacência:\n",
    #       grafo.matriz_adj)
    
    # # Verificar adjacentes
    # grafo.verificar_adjacencia()

    # #Verificar grau de um vértice 
    # grafo.verificar_grau()

    # #Buscar todos os vizinhos
    # grafo.verificar_vizinhos()

    #Visitar todas as arestas
    print("Arestas do grafo:", grafo.visitar_arestas())

    # Aplicação de busca
    ciclo = detectar_ciclos(grafo.matriz_adj, grafo.dirigido)
    print("O grafo", ciclo)

    # Gerar arquivo GEXF do grafo
    grafo.gerar_novo_arquivo()
    print("Novo arquivo GEXF gerado com sucesso!")


if __name__ == "__main__":
    main()