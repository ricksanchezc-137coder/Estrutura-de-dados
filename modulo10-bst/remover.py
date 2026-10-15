from bst_basico import BST

arvore = BST()
for v in [50, 30, 70, 20, 40, 60, 80, 65]:
    arvore.inserir(v)


def mostrar(titulo, resultado=None):
    lista = arvore.em_ordem()
    print(titulo, "->", resultado)
    print("  em-ordem:", lista)
    print("  len:", len(arvore), "| raiz:", arvore.raiz.valor,
          "| ordenada:", lista == sorted(lista))


mostrar("inicial")
mostrar("remover 20 (folha)", arvore.remover(20))
mostrar("remover 60 (um filho)", arvore.remover(60))
mostrar("remover 50 (dois filhos, raiz)", arvore.remover(50))
mostrar("remover 99 (nao existe)", arvore.remover(99))

vazia = BST()
print("remover em vazia:", vazia.remover(5), len(vazia))
