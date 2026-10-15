from bst_basico import BST, No


def eh_bst_ingenua(no):
    if no is None:
        return True
    if no.esquerda is not None and no.esquerda.valor >= no.valor:
        return False
    if no.direita is not None and no.direita.valor <= no.valor:
        return False
    return eh_bst_ingenua(no.esquerda) and eh_bst_ingenua(no.direita)


def eh_bst(no, minimo=None, maximo=None):
    if no is None:
        return True
    if minimo is not None and no.valor <= minimo:
        return False
    if maximo is not None and no.valor >= maximo:
        return False
    return (eh_bst(no.esquerda, minimo, no.valor)
            and eh_bst(no.direita, no.valor, maximo))


def mostrar(titulo, raiz):
    print(f"{titulo}: ingenua={eh_bst_ingenua(raiz)} | com limites={eh_bst(raiz)}")


valida = BST()
for v in [50, 30, 70, 20, 40, 60, 80]:
    valida.inserir(v)
mostrar("valida", valida.raiz)

mostrar("vazia", None)
mostrar("um no", No(7))

# 10 com filhos 5 e 15; o 15 tem filho esquerdo 6 (menor que 15, mas menor que 10 tambem)
armadilha = No(10)
armadilha.esquerda = No(5)
armadilha.direita = No(15)
armadilha.direita.esquerda = No(6)
armadilha.direita.direita = No(20)
mostrar("armadilha", armadilha)

arvore_armadilha = BST()
arvore_armadilha.raiz = armadilha
print("em-ordem da armadilha:", arvore_armadilha.em_ordem())

erro_local = No(10)
erro_local.esquerda = No(20)
mostrar("erro local", erro_local)

mostrar("equilibrada", BST.de_lista_ordenada(list(range(100))).raiz)
