from bfs import montar_exemplo


def dfs_recursivo(grafo, inicio):
    visitados = set()
    ordem = []

    def visitar(v):
        visitados.add(v)
        ordem.append(v)
        for w in grafo[v]:
            if w not in visitados:
                visitar(w)

    visitar(inicio)
    return ordem


def dfs_iterativo(grafo, inicio):
    visitados = set()
    ordem = []
    pilha = [inicio]
    while pilha:
        v = pilha.pop()
        if v in visitados:
            continue
        visitados.add(v)
        ordem.append(v)
        for w in reversed(grafo[v]):
            if w not in visitados:
                pilha.append(w)
    return ordem


if __name__ == "__main__":
    g = montar_exemplo()
    for inicio in ["A", "E"]:
        r = dfs_recursivo(g, inicio)
        i = dfs_iterativo(g, inicio)
        print(f"dfs de {inicio}: recursivo {r} | iterativo {i} | iguais: {r == i}")
