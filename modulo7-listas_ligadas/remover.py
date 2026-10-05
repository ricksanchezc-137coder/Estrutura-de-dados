from lista_simples import ListaSimples

lista = ListaSimples()
for v in (1, 2, 3, 4, 5):
    lista.inserir_fim(v)
print("inicial:", lista, "len:", len(lista))

print("3 in lista:", 3 in lista, "| 99 in lista:", 99 in lista)

print("remover(1) [cabeça] ->", lista.remover(1), lista, "len:", len(lista))
print("remover(3) [meio]   ->", lista.remover(3), lista, "len:", len(lista))
print("remover(5) [fim]    ->", lista.remover(5), lista, "len:", len(lista))
print("remover(99) [não existe] ->", lista.remover(99), lista, "len:", len(lista))

vazia = ListaSimples()
print("remover em vazia ->", vazia.remover(1), vazia, "len:", len(vazia))
