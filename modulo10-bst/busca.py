from bst_basico import BST

arvore = BST()
for v in [50, 30, 70, 20, 40, 60, 80]:
    arvore.inserir(v)

for alvo in [40, 60, 99, 10, 85]:
    print(f"{alvo} in arvore:", alvo in arvore)

print("minimo:", arvore.minimo())
print("maximo:", arvore.maximo())

try:
    BST().minimo()
except ValueError as e:
    print("vazia, erro:", e)

um = BST()
um.inserir(7)
print("um no:", um.minimo(), um.maximo())
