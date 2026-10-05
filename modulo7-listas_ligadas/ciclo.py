from lista_simples import ListaSimples


def tem_ciclo(lista):
    lento = rapido = lista.cabeca
    while rapido is not None and rapido.proximo is not None:
        lento = lento.proximo
        rapido = rapido.proximo.proximo
        if lento is rapido:
            return True
    return False


def montar(*valores):
    lista = ListaSimples()
    for v in valores:
        lista.inserir_fim(v)
    return lista


lista = montar(1, 2, 3, 4, 5)
print("sem ciclo:", tem_ciclo(lista))

terceiro = lista.cabeca.proximo.proximo
ultimo = terceiro.proximo.proximo
ultimo.proximo = terceiro
print("com ciclo (5 aponta pro 3):", tem_ciclo(lista))

print("vazia:", tem_ciclo(ListaSimples()))

um = montar(7)
print("um elemento:", tem_ciclo(um))
um.cabeca.proximo = um.cabeca
print("um elemento apontando pra si:", tem_ciclo(um))
