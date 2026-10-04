import timeit

t = (1, 2, 3)
print("tupla antes:", id(t))
t += (4,)
print("tupla depois:", id(t), t)

lista = [1, 2, 3]
print("lista antes:", id(lista))
lista += [4]
print("lista depois:", id(lista), lista)


def construir_tupla(n):
    t = ()
    for i in range(n):
        t += (i,)
    return t


for n in (5_000, 10_000, 20_000, 40_000):
    tempo = min(timeit.repeat(lambda: construir_tupla(n), number=1, repeat=3))
    print(f"n={n} tempo={tempo:.4f}s")
