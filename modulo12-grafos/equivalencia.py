import random
from grafo_lista import GrafoLista
from grafo_matriz import GrafoMatriz


def comparar(direcionado, n, operacoes, semente):
    rnd = random.Random(semente)
    gl = GrafoLista(direcionado=direcionado)
    gm = GrafoMatriz(direcionado=direcionado)
    for v in range(n):
        gl.adicionar_vertice(v)
        gm.adicionar_vertice(v)

    div = 0
    for _ in range(operacoes):
        u, v = rnd.sample(range(n), 2)
        if rnd.random() < 0.7:
            peso = rnd.randint(1, 9)
            gl.adicionar_aresta(u, v, peso)
            gm.adicionar_aresta(u, v, peso)
        elif gl.remover_aresta(u, v) != gm.remover_aresta(u, v):
            div += 1

    for u in range(n):
        if sorted(gl.vizinhos(u)) != sorted(gm.vizinhos(u)):
            div += 1
        if gl.grau(u) != gm.grau(u):
            div += 1
        if gl.grau_entrada(u) != gm.grau_entrada(u):
            div += 1
        for v in range(n):
            if u == v:
                continue
            if gl.tem_aresta(u, v) != gm.tem_aresta(u, v):
                div += 1
            elif gl.tem_aresta(u, v) and gl.peso(u, v) != gm.peso(u, v):
                div += 1
    if gl.num_arestas() != gm.num_arestas():
        div += 1
    if len(gl) != len(gm):
        div += 1
    return div, gl.num_arestas()


for direcionado in (False, True):
    for n, ops in [(5, 20), (30, 300), (100, 2000)]:
        div, arestas = comparar(direcionado, n, ops, semente=42)
        print(f"direcionado={direcionado} n={n} ops={ops}: divergencias={div} arestas={arestas}")
