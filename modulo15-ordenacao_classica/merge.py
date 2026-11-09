def intercalar(esq, direita):
    resultado = []
    i = j = 0
    comparacoes = 0
    while i < len(esq) and j < len(direita):
        comparacoes += 1
        if esq[i] <= direita[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(direita[j:])
    return resultado, comparacoes


def merge_sort(lista):
    if len(lista) <= 1:
        return list(lista), 0
    meio = len(lista) // 2
    esq, ce = merge_sort(lista[:meio])
    direita, cd = merge_sort(lista[meio:])
    resultado, cm = intercalar(esq, direita)
    return resultado, ce + cd + cm


if __name__ == "__main__":
    casos = {
        "aleatória": [5, 2, 9, 1, 7],
        "já ordenada": [1, 2, 3, 4, 5],
        "invertida": [5, 4, 3, 2, 1],
        "vazia": [],
        "um item": [7],
    }
    for nome, dados in casos.items():
        original = list(dados)
        ordenada, c = merge_sort(dados)
        print(f"{nome}: {ordenada} ({c}) | original intacta: {dados == original}")
