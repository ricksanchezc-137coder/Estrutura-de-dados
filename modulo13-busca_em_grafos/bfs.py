from collections import deque


def montar_exemplo():
    return {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"],
    }


def bfs(grafo, inicio):
    visitados = {inicio}
    fila = deque([inicio])
    ordem = []
    while fila:
        v = fila.popleft()
        ordem.append(v)
        for w in grafo[v]:
            if w not in visitados:
                visitados.add(w)
                fila.append(w)
    return ordem


if __name__ == "__main__":
    g = montar_exemplo()
    print("bfs de A:", bfs(g, "A"))
    print("bfs de E:", bfs(g, "E"))

    g["F"] = []
    print("com F isolado, bfs de A:", bfs(g, "A"))
    print("bfs de F:", bfs(g, "F"))
