import timeit

def tem_duplicata(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

for n in [500, 1000, 2000, 4000]:
    dados = list(range(n))
    t = min(timeit.repeat(lambda: tem_duplicata(dados), number=1, repeat=3))
    print(f"n={n:>5} {t:.4f}s")
