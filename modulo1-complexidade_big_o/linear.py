import timeit

def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total

for n in [10_000, 20_000, 40_000, 80_000]:
    dados = list(range(n))
    t = min(timeit.repeat(lambda: soma(dados), number=100, repeat=5))
    print(f"n={n:>6} {t:.4f}s")
