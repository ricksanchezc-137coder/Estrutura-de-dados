from collections import deque
from bfs import montar_exemplo


def distancias(grafo, inicio):
    dist = {inicio: 0}
    fila = deque([inicio])
    while fila:
        v = fila.popleft()
        for w in grafo[v]:
            if w not in dist:
                dist[w] = dist[v] + 1
                fila.append(w)
    return dist


def menor_caminho(grafo, origem, destino):
    pai = {origem: None}
    fila = deque([origem])
    while fila:
        v = fila.popleft()
        if v == destino:
            break
        for w in grafo[v]:
            if w not in pai:
                pai[w] = v
                fila.append(w)
    if destino not in pai:
        return None
    caminho = []
    v = destino
    while v is not None:
        caminho.append(v)
        v = pai[v]
    caminho.reverse()
    return caminho


if __name__ == "__main__":
    g = montar_exemplo()
    g["F"] = []
    print("distancias de A:", distancias(g, "A"))
    print("A -> E:", menor_caminho(g, "A", "E"))
    print("E -> A:", menor_caminho(g, "E", "A"))
    print("A -> A:", menor_caminho(g, "A", "A"))
    print("A -> F:", menor_caminho(g, "A", "F"))
