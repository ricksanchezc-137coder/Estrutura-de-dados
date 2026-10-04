import sys

print("n | lista (append) | lista (list) | tupla")
for n in (0, 1, 5, 10, 100):
    lista_append = []
    for i in range(n):
        lista_append.append(i)

    lista_direta = list(range(n))
    tupla = tuple(range(n))

    print(
        f"{n} | {sys.getsizeof(lista_append)} | "
        f"{sys.getsizeof(lista_direta)} | {sys.getsizeof(tupla)}"
    )

