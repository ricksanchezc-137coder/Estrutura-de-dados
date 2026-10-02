import timeit
from bisect import bisect_left

def busca_binaria(lista, alvo):
    i = bisect_left(lista, alvo)
    return i < len(lista) and lista[i] == alvo

for n in [10_000, 100_000, 1_000_000]:
    lista = list(range(n))
    alvo = n
    t = min(timeit.repeat(lambda: busca_binaria(lista, alvo), number=100_000, repeat=5))
    print(f"n={n:>8} bisect {t:.6f}s")
