import timeit
from itertools import islice
from lista_simples import ListaSimples
from lista_dupla import ListaDupla


def montar(cls, n):
    lista = cls()
    for i in range(n):
        lista.inserir_fim(i)
    return lista


print("(A) n inserções no fim: simples / dupla")
for n in (1000, 2000, 4000, 8000):
    t_s = min(timeit.repeat(lambda: montar(ListaSimples, n), number=1, repeat=3))
    t_d = min(timeit.repeat(lambda: montar(ListaDupla, n), number=1, repeat=3))
    print(f"n={n}: simples {t_s:.4f}s / dupla {t_d:.4f}s")

print("(B) 100 acessos ao item do meio: list / ligada")
for n in (10000, 20000, 40000, 80000):
    base = list(range(n))
    ligada = montar(ListaDupla, n)
    meio = n // 2
    t_l = min(timeit.repeat(lambda: base[meio], number=100, repeat=3))
    t_g = min(timeit.repeat(lambda: next(islice(ligada, meio, None)), number=100, repeat=3))
    print(f"n={n}: list {t_l:.6f}s / ligada {t_g:.6f}s")
