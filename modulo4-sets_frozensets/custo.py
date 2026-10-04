# modulo4-sets_frozensets/custo.py
import timeit


def medir(func, number=1, repeat=3):
    return min(timeit.repeat(func, number=number, repeat=repeat))


# A) construir um set com n chamadas de add()
print("A) add n elementos")
for n in [100_000, 200_000, 400_000, 800_000]:
    def construir():
        s = set()
        for i in range(n):
            s.add(i)

    print(f"n={n}: {medir(construir):.4f}s")

# B) interseção: set pequeno fixo (1000) com set grande crescendo
print("B) interseção pequeno x grande (1000 chamadas)")
pequeno = set(range(1000))
for n in [100_000, 200_000, 400_000, 800_000]:
    grande = set(range(n))
    t = medir(lambda: pequeno & grande, number=1000, repeat=5)
    print(f"n={n}: {t * 1000:.3f} ms")

# C) remove vs discard num elemento ausente
print("C) remove vs discard")
s = {1, 2, 3}
s.discard(99)
print("discard(99): sem erro,", s)
try:
    s.remove(99)
except KeyError as e:
    print("KeyError:", e)
