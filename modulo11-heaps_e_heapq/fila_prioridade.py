import heapq
from itertools import count


class Tarefa:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Tarefa({self.nome})"


# 1) max-heap guardando valores negativos
heap = []
for x in [5, 3, 8, 1, 9, 2]:
    heapq.heappush(heap, -x)
print("maior:", -heap[0])
print("saida:", [-heapq.heappop(heap) for _ in range(len(heap))])

# 2) tuplas (prioridade, tarefa)
fila = []
heapq.heappush(fila, (2, "lavar louca"))
heapq.heappush(fila, (1, "pagar conta"))
heapq.heappush(fila, (3, "estudar"))
print("tuplas:", [heapq.heappop(fila) for _ in range(len(fila))])

# 3) prioridades iguais com objetos sem comparacao
fila = []
heapq.heappush(fila, (1, Tarefa("a")))
try:
    heapq.heappush(fila, (1, Tarefa("b")))
except TypeError as e:
    print("erro:", e)

# 4) desempate com contador
contador = count()
fila = []
for prioridade, nome in [(1, "a"), (2, "b"), (1, "c"), (1, "d")]:
    heapq.heappush(fila, (prioridade, next(contador), Tarefa(nome)))
saida = []
while fila:
    prioridade, _, tarefa = heapq.heappop(fila)
    saida.append((prioridade, tarefa))
print("com contador:", saida)
