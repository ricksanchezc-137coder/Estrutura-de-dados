import sys

d = {}
anterior = sys.getsizeof(d)
print(f"len=0: {anterior} bytes")

for i in range(60):
    d[i] = i
    atual = sys.getsizeof(d)
    if atual != anterior:
        print(f"len={len(d)}: {atual} bytes")
        anterior = atual
