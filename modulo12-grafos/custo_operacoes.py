import timeit


def estrela_lista(n):
    g = {i: [] for i in range(n)}
    for i in range(1, n):
        g[0].append(i)
        g[i].append(0)
    return g


def estrela_matriz(n):
    m = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[0][i] = 1
        m[i][0] = 1
    return m


def tem_aresta_lista(g, u, v):
    return v in g[u]


def tem_aresta_matriz(m, u, v):
    return m[u][v] == 1


def vizinhos_lista(g, u):
    return list(g[u])


def vizinhos_matriz(m, u):
    return [j for j in range(len(m)) if m[u][j]]


# conferencia: as duas estruturas devem dar o mesmo resultado
g5, m5 = estrela_lista(5), estrela_matriz(5)
print("vizinhos de 0 iguais:", vizinhos_lista(g5, 0) == vizinhos_matriz(m5, 0))
print("vizinhos de 1 iguais:", vizinhos_lista(g5, 1) == vizinhos_matriz(m5, 1))
print("aresta 0-4:", tem_aresta_lista(g5, 0, 4), tem_aresta_matriz(m5, 0, 4))
print("aresta 1-2:", tem_aresta_lista(g5, 1, 2), tem_aresta_matriz(m5, 1, 2))
print()


def us(funcao, vezes=2000):
    return min(timeit.repeat(funcao, number=vezes, repeat=3)) / vezes * 1e6


print("n | aresta lista | aresta matriz | vizinhos lista | vizinhos matriz  (us por chamada)")
for n in [250, 500, 1000, 2000]:
    g, m = estrela_lista(n), estrela_matriz(n)
    a_l = us(lambda: tem_aresta_lista(g, 0, n - 1))
    a_m = us(lambda: tem_aresta_matriz(m, 0, n - 1))
    v_l = us(lambda: vizinhos_lista(g, 1))
    v_m = us(lambda: vizinhos_matriz(m, 1))
    print(f"{n} | {a_l:.3f} | {a_m:.3f} | {v_l:.3f} | {v_m:.3f}")
