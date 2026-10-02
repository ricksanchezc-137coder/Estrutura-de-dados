import timeit

for n in [10_000, 100_000, 1_000_000]:
    lista = list(range(n))
    conjunto = set(lista)
    alvo = -1
    t_lista = min(timeit.repeat(lambda: alvo in lista, number=100, repeat=5))
    t_set = min(timeit.repeat(lambda: alvo in conjunto, number=100, repeat=5))
    print(f"n={n:>8} lista {t_lista:.6f}s set {t_set:.6f}s")

