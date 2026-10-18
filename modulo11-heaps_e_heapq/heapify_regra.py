import heapq


def eh_heap(lista):
    for i in range(len(lista)):
        for filho in (2 * i + 1, 2 * i + 2):
            if filho < len(lista) and lista[i] > lista[filho]:
                return False
    return True


dados = [9, 5, 8, 1, 3, 2]
print("antes:", dados, "| eh heap:", eh_heap(dados))
heapq.heapify(dados)
print("depois:", dados, "| eh heap:", eh_heap(dados))
print("heap[0]:", dados[0])

print("pai do indice 5:", (5 - 1) // 2)
print("filhos do indice 1:", 2 * 1 + 1, 2 * 1 + 2)

h = [1, 3, 2, 5, 9, 8]
print("h:", h, "| eh heap:", eh_heap(h))
h.sort()
print("apos sort:", h, "| eh heap:", eh_heap(h))

print("[5, 3, 8] eh heap:", eh_heap([5, 3, 8]))
