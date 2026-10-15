from timeit import repeat
from bst_basico import BST

arvore = BST()
for v in [50, 30, 70, 20, 40, 60, 80, 65]:
    arvore.inserir(v)

print("em-ordem:", arvore.em_ordem())
print("sucessor de 50:", arvore.sucessor(50))
print("sucessor de 80:", arvore.sucessor(80))
print("sucessor de 45 (ausente):", arvore.sucessor(45))
print("sucessor de 10 (ausente):", arvore.sucessor(10))
print("predecessor de 50:", arvore.predecessor(50))
print("predecessor de 20:", arvore.predecessor(20))
print("predecessor de 65:", arvore.predecessor(65))
print("predecessor de 66 (ausente):", arvore.predecessor(66))
print("predecessor de 100 (ausente):", arvore.predecessor(100))

print("intervalo(35, 65):", arvore.intervalo(35, 65))
print("intervalo(0, 100):", arvore.intervalo(0, 100))
print("intervalo(81, 90):", arvore.intervalo(81, 90))
print("intervalo(61, 64):", arvore.intervalo(61, 64))
print("intervalo(60, 60):", arvore.intervalo(60, 60))
print("vazia intervalo(1, 5):", BST().intervalo(1, 5))

grande = BST.de_lista_ordenada(list(range(100000)))
print("grande intervalo(50000, 50010):", grande.intervalo(50000, 50010))

t_poda = min(repeat(lambda: grande.intervalo(50000, 50010),
                    number=1000, repeat=3)) / 1000
t_filtro = min(repeat(lambda: [x for x in grande.em_ordem() if 50000 <= x <= 50010],
                      number=5, repeat=3)) / 5
print(f"intervalo com poda: {t_poda * 1e6:.1f} us por chamada")
print(f"em_ordem + filtro: {t_filtro * 1e3:.2f} ms por chamada")
print(f"razao: {t_filtro / t_poda:.0f}x")
