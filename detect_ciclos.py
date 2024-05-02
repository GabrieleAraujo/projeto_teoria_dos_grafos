
# Aplicação de busca - detecção de ciclos
def detectar_ciclos(matriz_adj, tipo_grafo):
    n = len(matriz_adj)
    visitado = [False] * n

    # DFS em grafos dirigidos
    def ciclo_dirigido(v, rec_stack):
        if not visitado[v]:
            visitado[v] = True
            rec_stack[v] = True
            for i in range(n):
                if matriz_adj[v][i] != 0:
                    if not visitado[i] and ciclo_dirigido(i, rec_stack):
                        return True
                    elif rec_stack[i]:
                        return True
        rec_stack[v] = False
        return False

    #Grafos não dirigidos
    def ciclo_nao_dirigido(v, pai):
        visitado[v] = True
        for i in range(n):
            if matriz_adj[v][i] != 0:
                if not visitado[i]:
                    if ciclo_nao_dirigido(i, v):
                        return True
                elif i != pai:
                    return True
        return False

    # Tipo de grafo
    if tipo_grafo:
        rec_stack = [False] * n
        for node in range(n):
            if not visitado[node]:
                if ciclo_dirigido(node, rec_stack):
                    return "contém ciclo"
    else:
        for node in range(n):
            if not visitado[node]:
                if ciclo_nao_dirigido(node, -1):  # -1 representa 'sem pai'
                    return "contém ciclo"

    return "não contém ciclo"

