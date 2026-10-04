import timeit 

def construir_no_inicio(n):
    lista = []
    for i in range(n):
        lista.insert(0, i)
    return lista

for n in (10_000, 20_000, 40_000, 80_000):
    t = min(timeit.repeat(lambda: construir_no_inicio(n), number=1, repeat=3))
    print(f"n={n} tempo={t:.4f}s")
