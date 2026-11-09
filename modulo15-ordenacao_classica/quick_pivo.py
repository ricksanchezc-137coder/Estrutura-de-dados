import random


def escolher(lista, ini, fim, estrategia):
    if estrategia == "ultimo":
        return fim
    if estrategia == "aleatorio":
        return random.randint(ini, fim)
    meio = (ini + fim) // 2
    trio = sorted([(lista[ini], ini), (lista[meio], meio), (lista[fim], fim)])
    return trio[1][1]


def quicksort(lista, estrategia="ultimo"):
    comparacoes = 0

    def ordenar(ini, fim):
        nonlocal comparacoes
        if ini >= fim:
            return
        p = escolher(lista, ini, fim, estrategia)
        lista[p], lista[fim] = lista[fim], lista[p]
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
    random.seed(42)
    geradores = {
        "ordenada": lambda n: list(range(n)),
        "invertida": lambda n: list(range(n, 0, -1)),
    }
    for nome, gerar in geradores.items():
        print(nome)
        for n in [1000, 2000, 4000, 8000, 16000]:
            linha = f"n={n}:"
            ok = True
            for est in ["mediana3", "aleatorio"]:
                dados = gerar(n)
                c = quicksort(dados, est)
                ok = ok and dados == sorted(dados)
                linha += f" {est} {c} ({c / n:.2f}) |"
            print(linha, "ordenou:", ok)
