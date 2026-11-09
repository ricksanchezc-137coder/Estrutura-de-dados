def quicksort(lista):
    comparacoes = 0

    def ordenar(ini, fim):
        nonlocal comparacoes
        if ini >= fim:
            return
        pivo = lista[fim]
        i = ini
        for j in range(ini, fim):
            comparacoes += 1
            if lista[j] < pivo:
                lista[i], lista[j] = lista[j], lista[i]
                i += 1
        lista[i], lista[fim] = lista[fim], lista[i]
        ordenar(ini, i - 1)
        ordenar(i + 1, fim)

    ordenar(0, len(lista) - 1)
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
        copia = list(dados)
        c = quicksort(copia)
        print(f"{nome}: {copia} ({c}) | original: {dados}")
