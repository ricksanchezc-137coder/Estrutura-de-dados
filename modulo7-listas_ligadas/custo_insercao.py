import timeit
from lista_simples import ListaSimples


def montar_inicio(n):
    lista = ListaSimples()
    for i in range(n):
        lista.inserir_inicio(i)


def montar_fim(n):
    lista = ListaSimples()
    for i in range(n):
        lista.inserir_fim(i)


if __name__ == "__main__":
    pequena = ListaSimples()
    for v in (1, 2, 3):
        pequena.inserir_fim(v)
    print("inserir_fim 1, 2, 3 ->", pequena, "len:", len(pequena))

    print("n, inicio, fim")
    for n in (1000, 2000, 4000, 8000):
        t_ini = min(timeit.repeat(lambda: montar_inicio(n), number=1, repeat=3))
        t_fim = min(timeit.repeat(lambda: montar_fim(n), number=1, repeat=3))
        print(f"n={n}: inicio {t_ini:.4f}s / fim {t_fim:.4f}s")
