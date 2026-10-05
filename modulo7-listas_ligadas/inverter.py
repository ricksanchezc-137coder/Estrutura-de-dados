from lista_simples import ListaSimples


def montar(*valores):
    lista = ListaSimples()
    for v in valores:
        lista.inserir_fim(v)
    return lista


lista = montar(1, 2, 3, 4, 5)
print("antes:", lista, "len:", len(lista))
lista.inverter()
print("depois:", lista, "len:", len(lista))
print("cabeca:", lista.cabeca.valor)
lista.inverter()
print("inverter 2x:", lista)

um = montar(7)
um.inverter()
print("um elemento:", um, "len:", len(um))

vazia = ListaSimples()
vazia.inverter()
print("vazia:", vazia, "len:", len(vazia))
