import random
from timeit import repeat
from bst_basico import BST


def montar(valores):
    arvore = BST()
    for v in valores:
        arvore.inserir(v)
    return arvore


random.seed(42)
for n in [500, 1000, 2000, 4000]:
    ordenados = list(range(n))
    aleatorios = random.sample(range(n * 10), n)
    t_ord = min(repeat(lambda: montar(ordenados), number=1, repeat=3))
    t_ale = min(repeat(lambda: montar(aleatorios), number=1, repeat=3))
    h_ord = montar(ordenados).altura()
    h_ale = montar(aleatorios).altura()
    print(f"n={n}: ordenado h={h_ord} {t_ord:.4f}s | aleatorio h={h_ale} {t_ale:.4f}s")
