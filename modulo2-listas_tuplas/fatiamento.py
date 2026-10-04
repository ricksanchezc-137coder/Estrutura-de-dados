import timeit

print("A) lista fixa, fatia cresce")
base = list(range(1_000_000))
for k in(100_000, 200_000, 400_000, 800_000):
    t = min(timeit.repeat(lambda: base[:k], number=20, repeat=5)) / 20
    print(f"k={k} tempo={t * 1000:.3f} ms")

print("B) fatia fixa (k=1000), lista cresce")
for n in (100_000, 200_000, 400_000, 800_000):
    base = list(range(n))
    t = min(timeit.repeat(lambda: base[:1000], number=2000, repeat=5)) / 2000
    print(f"n={n} tempo={t * 1e6:.2f} us")
