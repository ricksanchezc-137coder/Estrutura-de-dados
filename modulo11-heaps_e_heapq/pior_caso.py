import heapq
import random


class Contado:
    comparacoes = 0

    def __init__(self, valor):
        self.valor = valor

    def __lt__(self, outro):
        Contado.comparacoes += 1
        return self.valor < outro.valor


def contar_pushes(dados):
    Contado.comparacoes = 0
    heap = []
    for x in dados:
        heapq.heappush(heap, Contado(x))
    return Contado.comparacoes


random.seed(42)
for n in (1_000, 2_000, 4_000, 8_000, 16_000, 32_000):
    aleatorio = random.sample(range(n * 10), n)
    crescente = sorted(aleatorio)
    decrescente = crescente[::-1]
    r = [contar_pushes(d) / n for d in (aleatorio, crescente, decrescente)]
    print(f"n={n}: aleatorio {r[0]:.2f} | crescente {r[1]:.2f} | decrescente {r[2]:.2f}")
