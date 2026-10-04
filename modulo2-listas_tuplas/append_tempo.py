import timeit

def construir(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista

for n in (100_000, 200_000, 400_000, 800_000):
    t = min(timeit.repeat(lambda: construir(n), number=1, repeat=5))
    print(f"n={n} tempo={t:.4f}s")
