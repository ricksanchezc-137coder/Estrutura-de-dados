import heapq
import random


class Contado:
    comparacoes = 0

    def __init__(self, valor):
        self.valor = valor

    def __lt__(self, outro):
        Contado.comparacoes += 1
        return self.valor < outro.valor


def contar(funcao, dados):
    Contado.comparacoes = 0
    funcao([Contado(x) for x in dados])
    return Contado.comparacoes


def com_pushes(itens):
    heap = []
    for x in itens:
        heapq.heappush(heap, x)


def com_heapify(itens):
    heapq.heapify(itens)


random.seed(42)
for n in (1_000, 2_000, 4_000, 8_000, 16_000, 32_000):
    dados = random.sample(range(n * 10), n)
    c1 = contar(com_pushes, dados)
    c2 = contar(com_heapify, dados)
    print(f"n={n}: pushes {c1} ({c1 / n:.2f} por item) | heapify {c2} ({c2 / n:.2f} por item)")
