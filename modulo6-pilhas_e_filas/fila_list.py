from timeit import repeat

fila = []
for letra in ("A", "B", "C"):
    fila.append(letra)
    print(f"enqueue {letra}: {fila}")

for _ in range(3):
    saiu = fila.pop(0)
    print(f"dequeue -> {saiu}: {fila}")

def esvaziar(n):
    fila = list(range(n))
    while fila:
        fila.pop(0)

print()
anterior = None
for n in (10000, 20000, 40000, 80000):
    tempo = min(repeat(lambda: esvaziar(n), number=1, repeat=3))
    if anterior is None:
        print(f"n={n}: {tempo:.4f}s")
    else:
        print(f"n={n}: {tempo:.4f}s (razao: {tempo / anterior:.1f}x)")
    anterior = tempo
