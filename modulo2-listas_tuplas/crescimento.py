import sys

lista = []
anterior = sys.getsizeof(lista)
print(f"len=0 tamanho={anterior} bytes")

for i in range(1, 65):
    lista.append(i)
    atual = sys.getsizeof(lista)
    if atual != anterior:
        print(f"len={i} tamanho={atual} bytes")
        anterior = atual
