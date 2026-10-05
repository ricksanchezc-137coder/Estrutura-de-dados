# modulo6-pilhas_e_filas/fila_deque.py

from collections import deque
from timeit import repeat

# 1. Ordem FIFO
fila = deque()
for letra in ("A", "B", "C"):
    fila.append(letra)
    print(f"enqueue {letra}: {fila}")

for _ in range(3):
    saiu = fila.popleft()
    print(f"dequeue -> {saiu}: {fila}")


# 2. Comparação list vs deque
def esvaziar_list(n):
    fila = list(range(n))
    while fila:
        fila.pop(0)


def esvaziar_deque(n):
    fila = deque(range(n))
    while fila:
        fila.popleft()


print()
for n in (10000, 20000, 40000, 80000):
    t_list = min(repeat(lambda: esvaziar_list(n), number=1, repeat=3))
    t_deque = min(repeat(lambda: esvaziar_deque(n), number=1, repeat=3))
    print(f"n={n}: list {t_list:.4f}s | deque {t_deque:.4f}s | deque {t_list / t_deque:.0f}x mais rápido")

# 3. Só deque, n maiores
print()
anterior = None
for n in (160000, 320000, 640000):
    tempo = min(repeat(lambda: esvaziar_deque(n), number=1, repeat=3))
    if anterior is None:
        print(f"n={n}: {tempo:.4f}s")
    else:
        print(f"n={n}: {tempo:.4f}s (razão: {tempo / anterior:.1f}x)")
    anterior = tempo
