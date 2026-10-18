import timeit
from grafo_lista import GrafoLista


def estrela_classe(n):
    g = GrafoLista()
    for i in range(1, n):
        g.adicionar_aresta(0, i)
    return g


def estrela_listas(n):
    g = {i: [] for i in range(n)}
    for i in range(1, n):
        g[0].append(i)
        g[i].append(0)
    return g


# conferencia
gc, gl = estrela_classe(5), estrela_listas(5)
print("vizinhos de 0 iguais:", gc.vizinhos(0) == gl[0])
print("aresta 0-4:", gc.tem_aresta(0, 4), 4 in gl[0])
print("aresta 1-2:", gc.tem_aresta(1, 2), 2 in gl[1])
print()


def us(funcao, vezes=200):
    return min(timeit.repeat(funcao, number=vezes, repeat=3)) / vezes * 1e6


print("n | aresta dict | aresta lista | vizinhos(0) dict | vizinhos(0) lista  (us por chamada)")
for n in [1000, 4000, 16000, 64000]:
    gc, gl = estrela_classe(n), estrela_listas(n)
    a_d = us(lambda: gc.tem_aresta(0, n - 1))
    a_l = us(lambda: (n - 1) in gl[0])
    v_d = us(lambda: gc.vizinhos(0))
    v_l = us(lambda: list(gl[0]))
    print(f"{n} | {a_d:.3f} | {a_l:.3f} | {v_d:.3f} | {v_l:.3f}")
