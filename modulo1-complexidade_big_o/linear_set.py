import timeit

def tem_duplicata_set(lista):
    vistos = set()
    for x in lista:
        if x in vistos:
            return True
    return False

for n in [4000, 8000, 16000, 32000]:
    dados = list(range(n))
    t = min(timeit.repeat(lambda: tem_duplicata_set(dados), number=1, repeat=3))
    print(f"n={n:>6} {t:.5f}s")

