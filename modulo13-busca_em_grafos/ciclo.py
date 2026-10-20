from bfs import montar_exemplo
from dfs_vs_bfs import montar_anel


def tem_ciclo(grafo):
    visitados = set()
    for inicio in grafo:
        if inicio in visitados:
            continue
        visitados.add(inicio)
        pilha = [(inicio, None)]
        while pilha:
            v, pai = pilha.pop()
            for w in grafo[v]:
                if w == pai:
                    continue
                if w in visitados:
                    return True
                visitados.add(w)
                pilha.append((w, v))
    return False


if __name__ == "__main__":
    arvore = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A"],
        "D": ["B"],
        "E": ["B"],
    }
    triangulo_e_isolado = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
        "D": [],
    }
    ciclo_no_segundo = {
        "A": ["B"],
        "B": ["A"],
        "C": ["D", "E"],
        "D": ["C", "E"],
        "E": ["C", "D"],
    }
    print("exemplo:", tem_ciclo(montar_exemplo()))
    print("anel:", tem_ciclo(montar_anel()))
    print("arvore:", tem_ciclo(arvore))
    print("triangulo + isolado:", tem_ciclo(triangulo_e_isolado))
    print("ciclo so no 2o componente:", tem_ciclo(ciclo_no_segundo))
    print("um vertice:", tem_ciclo({"A": []}))
    print("vazio:", tem_ciclo({}))
