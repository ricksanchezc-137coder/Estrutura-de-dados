import timeit


def arestas_esparsas(n):
    return [(i, (i + 1) % n) for i in range(n)] + [(i, (i + 2) % n) for i in range(n)]


def montar_lista(n):
    g = {i: [] for i in range(n)}
    for u, v in arestas_esparsas(n):
        g[u].append(v)
        g[v].append(u)
    return g


def montar_matriz(n):
    m = [[0] * n for _ in range(n)]
    for u, v in arestas_esparsas(n):
        m[u][v] = 1
        m[v][u] = 1
    return m


tamanhos = [250, 500, 1000, 2000]

print("n | entradas na lista | celulas na matriz")
for n in tamanhos:
    g = montar_lista(n)
    entradas = sum(len(v) for v in g.values())
    print(n, "|", entradas, "|", n * n)

print()
print("n | lista (s) | matriz (s)")
for n in tamanhos:
    tl = min(timeit.repeat(lambda: montar_lista(n), number=1, repeat=3))
    tm = min(timeit.repeat(lambda: montar_matriz(n), number=1, repeat=3))
    print(f"{n} | {tl:.4f} | {tm:.4f}")
