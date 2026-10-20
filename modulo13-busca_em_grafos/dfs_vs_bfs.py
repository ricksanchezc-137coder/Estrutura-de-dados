from bfs import montar_exemplo
from menor_caminho import menor_caminho


def caminho_dfs(grafo, origem, destino):
    pai = {origem: None}

    def visitar(v):
        if v == destino:
            return True
        for w in grafo[v]:
            if w not in pai:
                pai[w] = v
                if visitar(w):
                    return True
        return False

    if not visitar(origem):
        return None
    caminho = []
    v = destino
    while v is not None:
        caminho.append(v)
        v = pai[v]
    caminho.reverse()
    return caminho


def montar_anel():
    return {
        "A": ["B", "E"],
        "B": ["A", "C"],
        "C": ["B", "D"],
        "D": ["C", "E"],
        "E": ["D", "A"],
    }


def mostrar(nome, grafo, origem, destino):
    b = menor_caminho(grafo, origem, destino)
    d = caminho_dfs(grafo, origem, destino)
    print(f"{nome} {origem} -> {destino}")
    print(f"  bfs: {b} ({len(b) - 1} arestas)")
    print(f"  dfs: {d} ({len(d) - 1} arestas)")


if __name__ == "__main__":
    mostrar("exemplo", montar_exemplo(), "A", "E")
    mostrar("anel", montar_anel(), "A", "E")
    mostrar("anel", montar_anel(), "A", "D")
