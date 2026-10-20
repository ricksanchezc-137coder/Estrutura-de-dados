from bfs import montar_exemplo


def componentes(grafo):
    visitados = set()
    resultado = []
    for inicio in grafo:
        if inicio in visitados:
            continue
        comp = []
        pilha = [inicio]
        visitados.add(inicio)
        while pilha:
            v = pilha.pop()
            comp.append(v)
            for w in grafo[v]:
                if w not in visitados:
                    visitados.add(w)
                    pilha.append(w)
        resultado.append(sorted(comp))
    return resultado


def eh_conexo(grafo):
    return len(componentes(grafo)) <= 1


def montar_tres():
    return {
        "A": ["B"],
        "B": ["A"],
        "C": ["D"],
        "D": ["C", "E"],
        "E": ["D"],
        "F": [],
    }


if __name__ == "__main__":
    g = montar_exemplo()
    print("exemplo:", componentes(g), "conexo:", eh_conexo(g))

    g["F"] = []
    print("com F:", componentes(g), "conexo:", eh_conexo(g))

    t = montar_tres()
    print("tres:", componentes(t), "conexo:", eh_conexo(t))
    print("vazio:", componentes({}), "conexo:", eh_conexo({}))
