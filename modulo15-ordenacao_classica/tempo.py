import heapq
import random
import time

from bubble import bubble_sort
from selection_insertion import selection_sort, insertion_sort
from merge import merge_sort
from quick_pivo import quicksort


def heap(lista):
    h = list(lista)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(lista))]


def medir(f, dados):
    copia = list(dados)
    inicio = time.perf_counter()
    f(copia)
    return time.perf_counter() - inicio


quick = lambda l: quicksort(l, "aleatorio")

random.seed(42)

todos = {"bubble": bubble_sort, "selection": selection_sort,
         "insertion": insertion_sort, "merge": merge_sort,
         "quick": quick, "heap": heap, "sorted": sorted}

for n in [500, 1000, 2000, 4000]:
    dados = random.sample(range(n * 10), n)
    print(f"aleatória n={n}")
    for nome, f in todos.items():
        print(f"  {nome}: {medir(f, dados):.4f}s")

rapidos = {k: todos[k] for k in ["merge", "quick", "heap", "sorted"]}
dados = random.sample(range(1_000_000), 100_000)
print("aleatória n=100000 (só os rápidos)")
for nome, f in rapidos.items():
    print(f"  {nome}: {medir(f, dados):.4f}s")

ordenada = list(range(100_000))
print("já ordenada n=100000")
for nome in ["bubble", "insertion", "merge", "quick", "heap", "sorted"]:
    print(f"  {nome}: {medir(todos[nome], ordenada):.4f}s")
