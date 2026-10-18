import heapq

heap = []
for x in [5, 3, 8, 1, 9, 2]:
    heapq.heappush(heap, x)
    print(f"push {x}: {heap}")

print("menor (heap[0]):", heap[0])
print("len:", len(heap))

saida = []
while heap:
    saida.append(heapq.heappop(heap))
print("pops em sequencia:", saida)

try:
    heapq.heappop(heap)
except IndexError as e:
    print("erro:", e)
