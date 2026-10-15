from travessias_dfs import No, em_ordem


def construir_equilibrada(valores, inicio=0, fim=None):
    if fim is None:
        fim = len(valores)
    if inicio >= fim:
        return None
    meio = (inicio + fim) // 2
    no = No(valores[meio])
    no.esquerda = construir_equilibrada(valores, inicio, meio)
    no.direita = construir_equilibrada(valores, meio + 1, fim)
    return no


def altura(no):
    if no is None:
        return -1
    return 1 + max(altura(no.esquerda), altura(no.direita))


if __name__ == "__main__":
    raiz = construir_equilibrada([1, 2, 3, 4, 5, 6, 7])
    print("raiz:", raiz.valor, "esq:", raiz.esquerda.valor, "dir:", raiz.direita.valor)
    print("em-ordem:", em_ordem(raiz))
    print("altura de 7:", altura(raiz))
    print("vazia:", construir_equilibrada([]))
    for n in (1000, 10000, 100000, 1000000):
        arv = construir_equilibrada(list(range(n)))
        print(f"n={n}: altura={altura(arv)}")
