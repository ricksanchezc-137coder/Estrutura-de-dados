from busca_binaria import busca_binaria


def busca_loop_infinito(lista, alvo, limite=50):
    inicio, fim = 0, len(lista) - 1
    passos = 0
    while inicio <= fim:
        passos += 1
        if passos > limite:
            raise RuntimeError(f"passou de {limite} passos")
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        if lista[meio] < alvo:
            inicio = meio  # BUG: faltou + 1
        else:
            fim = meio - 1
    return -1


def busca_off_by_one(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    while inicio < fim:  # BUG: deveria ser <=
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        if lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


print("--- A: loop infinito ---")
for alvo in [1, 5, 7, 8]:
    try:
        print(alvo, "->", busca_loop_infinito([1, 3, 5, 7], alvo))
    except RuntimeError as e:
        print(alvo, "-> RuntimeError:", e)

print("--- B: off-by-one ---")
dados = [1, 3, 5, 7]
for alvo in dados:
    print(alvo, "->", busca_off_by_one(dados, alvo), "(esperado", dados.index(alvo), ")")
print("[9] ->", busca_off_by_one([9], 9), "(esperado 0)")

print("--- C: lista fora de ordem ---")
bagunca = [5, 1, 9, 3, 7, 2]
for alvo in bagunca:
    print(alvo, "->", busca_binaria(bagunca, alvo), "(esperado", bagunca.index(alvo), ")")
