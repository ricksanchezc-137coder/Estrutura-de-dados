import heapq

dados = [5, 3, 8, 1, 9, 2, 7]
print("3 menores:", heapq.nsmallest(3, dados))
print("3 maiores:", heapq.nlargest(3, dados))
print("original:", dados)

pessoas = [("Ana", 31), ("Bia", 25), ("Caio", 40), ("Davi", 19)]
print("2 mais novos:", heapq.nsmallest(2, pessoas, key=lambda p: p[1]))
print("2 mais velhos:", heapq.nlargest(2, pessoas, key=lambda p: p[1]))

a = [1, 4, 9]
b = [2, 3, 10]
c = [5, 6, 7]
juntas = heapq.merge(a, b, c)
print("merge e lista?", isinstance(juntas, list))
print("merge:", list(juntas))


def heapsort(iteravel):
    heap = list(iteravel)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]


print("heapsort:", heapsort(dados))
print("igual ao sorted:", heapsort(dados) == sorted(dados))
print("vazio:", heapsort([]))
