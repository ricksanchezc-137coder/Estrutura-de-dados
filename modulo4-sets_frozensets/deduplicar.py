# modulo4-sets_frozensets/deduplicar.py
import timeit


def dedup_lista(xs):
    resultado = []
    for x in xs:
        if x not in resultado:
            resultado.append(x)
    return resultado


def dedup_set(xs):
    return list(set(xs))


def dedup_dict(xs):
    return list(dict.fromkeys(xs))


# 1. Ordem do resultado
dados = [3, 1, 3, 2, 1, 5, 2]
print("1) lista:", dedup_lista(dados))
print("   set:  ", dedup_set(dados))
print("   dict: ", dedup_dict(dados))

# 2. Desempenho (sem duplicatas = pior caso da versão com lista)
print("2) tempo por tamanho")
for n in [1000, 2000, 4000, 8000]:
    xs = list(range(n))
    t_lista = min(timeit.repeat(lambda: dedup_lista(xs), number=1, repeat=3))
    t_set = min(timeit.repeat(lambda: dedup_set(xs), number=1, repeat=3))
    t_dict = min(timeit.repeat(lambda: dedup_dict(xs), number=1, repeat=3))
    print(f"n={n}: lista={t_lista:.4f}s set={t_set:.6f}s dict={t_dict:.6f}s")
