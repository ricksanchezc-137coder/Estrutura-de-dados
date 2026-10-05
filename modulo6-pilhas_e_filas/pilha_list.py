pilha = []
for valor in (1, 2, 3):
    pilha.append(valor)
    print(f"push {valor}: {pilha}")

for _ in range(3):
    valor = pilha.pop()
    print(f"pop -> {valor}: {pilha}")

try:
    pilha.pop()
except IndexError as e:
    print("IndexError", e)
