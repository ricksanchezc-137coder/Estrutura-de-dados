import heapq
import random
from timeit import repeat


def com_pushes(dados):
    heap = []
    for x in dados:
        heapq.heappush(heap, x)
    return heap


def com_heapify(dados):
    copia = list(dados)
    heapq.heapify(copia)
    return copia


random.seed(42)
for n in (100_000, 150_000, 200_000, 300_000, 400_000, 600_000, 800_000):
    dados = random.sample(range(n * 10), n)
    t1 = min(repeat(lambda: com_pushes(dados), number=1, repeat=7))
    t2 = min(repeat(lambda: com_heapify(dados), number=1, repeat=7))
    print(f"n={n}: pushes {t1:.4f}s | heapify {t2:.4f}s")
