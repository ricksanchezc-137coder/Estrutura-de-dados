import timeit
from bisect import bisect_left
from busca_binaria import busca_binaria


def com_bisect(lista, x):
    i = bisect_left(lista, x)
    return i < len(lista) and lista[i] == x


for n in [10_000, 100_000, 1_000_000]:
    lista = list(range(n))
    alvo = n  # ausente e maior que todos (pior caso)
    t_lin = min(timeit.repeat(lambda: alvo in lista, number=100, repeat=3))
    t_bin = min(timeit.repeat(lambda: busca_binaria(lista, alvo), number=100, repeat=3))
    t_bis = min(timeit.repeat(lambda: com_bisect(lista, alvo), number=100, repeat=3))
    print(f"n={n}: in {t_lin:.6f}s | propria {t_bin:.6f}s | bisect {t_bis:.6f}s")
