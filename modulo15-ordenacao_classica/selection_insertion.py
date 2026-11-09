def selection_sort(lista):
    n = len(lista)
    comparacoes = 0
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return comparacoes


def insertion_sort(lista):
    comparacoes = 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if lista[j] > chave:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = chave
    return comparacoes


if __name__ == "__main__":
    casos = {
        "aleatória": [5, 2, 9, 1, 7],
        "já ordenada": [1, 2, 3, 4, 5],
        "invertida": [5, 4, 3, 2, 1],
        "vazia": [],
        "um item": [7],
    }
    for nome, dados in casos.items():
        s = list(dados)
        i = list(dados)
        cs = selection_sort(s)
        ci = insertion_sort(i)
        print(f"{nome}: selection {s} ({cs}) | insertion {i} ({ci})")
