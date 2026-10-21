import random
import timeit
from bisect import insort


def com_insort(valores):
    lista = []
    for v in valores:
        insort(lista, v)
    return lista


def com_sort(valores):
    lista = list(valores)
    lista.sort()
    return lista


for n in [10_000, 20_000, 40_000, 80_000]:
    random.seed(42)
    valores = random.sample(range(n * 10), n)
    ok = com_insort(valores) == com_sort(valores)
    t_ins = min(timeit.repeat(lambda: com_insort(valores), number=1, repeat=3))
    t_sort = min(timeit.repeat(lambda: com_sort(valores), number=1, repeat=3))
    print(f"n={n}: insort {t_ins:.4f}s | sort {t_sort:.4f}s | iguais {ok}")
