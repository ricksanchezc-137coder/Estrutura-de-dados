from travessias_dfs import No, montar_exemplo


def contar_nos(no):
    if no is None:
        return 0
    return 1 + contar_nos(no.esquerda) + contar_nos(no.direita)


def contar_folhas(no):
    if no is None:
        return 0
    if no.esquerda is None and no.direita is None:
        return 1
    return contar_folhas(no.esquerda) + contar_folhas(no.direita)


def altura(no):
    if no is None:
        return -1
    return 1 + max(altura(no.esquerda), altura(no.direita))


def descer_direita(n):
    raiz = No(1)
    atual = raiz
    for i in range(2, n + 1):
        atual.direita = No(i)
        atual = atual.direita
    return raiz


if __name__ == "__main__":
    raiz = montar_exemplo()
    print("exemplo:", contar_nos(raiz), contar_folhas(raiz), altura(raiz))
    print("subarvore esq:", contar_nos(raiz.esquerda), contar_folhas(raiz.esquerda), altura(raiz.esquerda))
    print("vazia:", contar_nos(None), contar_folhas(None), altura(None))
    print("um no:", contar_nos(No(7)), contar_folhas(No(7)), altura(No(7)))
    print("degenerada de 4:", contar_nos(descer_direita(4)), contar_folhas(descer_direita(4)), altura(descer_direita(4)))
