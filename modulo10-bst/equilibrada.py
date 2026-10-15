from timeit import repeat
from bst_basico import BST


def montar(valores):
    arvore = BST()
    for v in valores:
        arvore.inserir(v)
    return arvore


def tempo_busca(arvore, alvo):
    return min(repeat(lambda: [alvo in arvore for _ in range(1000)],
                      number=1, repeat=3))


for n in [1000, 2000, 4000]:
    ordenados = list(range(n))
    degenerada = montar(ordenados)
    equilibrada = BST.de_lista_ordenada(ordenados)
    print(f"n={n}")
    print(f"  degenerada:  h={degenerada.altura()}, 1000 buscas do ausente {n}: {tempo_busca(degenerada, n):.4f}s")
    print(f"  equilibrada: h={equilibrada.altura()}, 1000 buscas do ausente {n}: {tempo_busca(equilibrada, n):.4f}s")
    print(f"  em-ordem da equilibrada correta: {equilibrada.em_ordem() == ordenados}, len={len(equilibrada)}")

grande = BST.de_lista_ordenada(list(range(100000)))
print("n=100000 equilibrada: h =", grande.altura(),
      "| raiz:", grande.raiz.valor,
      "| 1000 buscas:", f"{tempo_busca(grande, 100000):.4f}s")
