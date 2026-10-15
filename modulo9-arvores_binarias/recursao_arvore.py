from travessias_dfs import No, pre_ordem, montar_exemplo


def descer_direita(n):
    raiz = No(1)
    atual = raiz
    for i in range(2, n + 1):
        atual.direita = No(i)
        atual = atual.direita
    return raiz


def pre_ordem_iterativa(raiz):
    if raiz is None:
        return []
    resultado = []
    pilha = [raiz]
    while pilha:
        no = pilha.pop()
        resultado.append(no.valor)
        if no.direita is not None:
            pilha.append(no.direita)
        if no.esquerda is not None:
            pilha.append(no.esquerda)
    return resultado


if __name__ == "__main__":
    raiz = montar_exemplo()
    print("recursiva:", pre_ordem(raiz))
    print("iterativa:", pre_ordem_iterativa(raiz))
    print("iguais:", pre_ordem(raiz) == pre_ordem_iterativa(raiz))
    print("vazia:", pre_ordem_iterativa(None))
    for n in (500, 900, 1000, 5000):
        arv = descer_direita(n)
        try:
            r = pre_ordem(arv)
            print(f"recursiva n={n}: ok, {len(r)} nos")
        except RecursionError:
            print(f"recursiva n={n}: RecursionError")
        r2 = pre_ordem_iterativa(arv)
        print(f"iterativa n={n}: ok, {len(r2)} nos")
