def bubble_sort(lista):
    n = len(lista)
    comparacoes = 0
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break
    return comparacoes

if __name__ == "__main__":
    a = [5, 2, 9, 1, 7]
    c = bubble_sort(a)
    print("ordenada:", a, "| comparações:", c)

    b = [1, 2, 3, 4, 5]
    print("já ordenada, comparações:", bubble_sort(b))

    d = [5, 4, 3, 2, 1]
    print("invertida, comparações:", bubble_sort(d))

    print("vazia:", bubble_sort([]), "| um item:", bubble_sort([7]))
