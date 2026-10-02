import random
import timeit

for n in [100_000, 200_000, 400_000, 800_000]:
    dados = [random.random() for _ in range(n)]
    t = min(timeit.repeat(lambda: sorted(dados), number=1, repeat=5))
    print(f"n={n:>7} {t:.4f}s")
