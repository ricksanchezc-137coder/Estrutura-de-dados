# modulo6-pilhas_e_filas/fila_propria.py

from collections import deque


class Fila:
    def __init__(self):
        self._itens = deque()

    def enqueue(self, valor):
        self._itens.append(valor)

    def dequeue(self):
        if self.esta_vazia():
            raise IndexError("fila vazia")
        return self._itens.popleft()

    def primeiro(self):
        if self.esta_vazia():
            raise IndexError("fila vazia")
        return self._itens[0]

    def esta_vazia(self):
        return len(self._itens) == 0

    def __len__(self):
        return len(self._itens)

    def __repr__(self):
        return f"Fila({list(self._itens)})"


f = Fila()
for letra in ("A", "B", "C"):
    f.enqueue(letra)
    print(f"enqueue {letra}: {f}")

print(f"primeiro: {f.primeiro()}, len: {len(f)}")

try:
    f[0]
except TypeError as erro:
    print(f"TypeError: {erro}")

while not f.esta_vazia():
    print(f"dequeue -> {f.dequeue()}: {f}")

try:
    f.dequeue()
except IndexError as erro:
    print(f"IndexError: {erro}")
