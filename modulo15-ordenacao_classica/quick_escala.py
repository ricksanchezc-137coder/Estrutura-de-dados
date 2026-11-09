import random
from quick import quicksort

print("aleatória (seed 42):")
for n in [1000, 2000, 4000, 8000, 16000]:
    random.seed(42)
    dados = random.sample(range(n * 10), n)
    c = quicksort(dados)
    print(f"n={n}: {c} ({c / n:.2f} por item) | ordenou: {dados == sorted(dados)}")

print("já ordenada:")
for n in [100, 200, 400, 800]:
    dados = list(range(n))
    c = quicksort(dados)
    print(f"n={n}: {c} | n(n-1)/2 = {n * (n - 1) // 2}")

print("limite de recursão, já ordenada:")
for n in [900, 1000, 5000]:
    try:
        quicksort(list(range(n)))
        print(f"n={n}: ok")
    except RecursionError:
        print(f"n={n}: RecursionError")
