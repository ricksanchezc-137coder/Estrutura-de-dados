def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

if __name__ == "__main__":
    dados = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    for alvo in [23, 2, 91, 7, 100]:
        print(alvo, "->", busca_binaria(dados, alvo))
    print("vazia:", busca_binaria([], 5))
