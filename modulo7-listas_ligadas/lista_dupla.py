class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class ListaDupla:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self._tamanho = 0

    def inserir_inicio(self, valor):
        no = NoDuplo(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = no
        else:
            no.proximo = self.cabeca
            self.cabeca.anterior = no
            self.cabeca = no
        self._tamanho += 1

    def inserir_fim(self, valor):
        no = NoDuplo(valor)
        if self.cauda is None:
            self.cabeca = self.cauda = no
        else:
            no.anterior = self.cauda
            self.cauda.proximo = no
            self.cauda = no
        self._tamanho += 1

    def remover_no(self, no):
        if no.anterior is None:
            self.cabeca = no.proximo
        else:
            no.anterior.proximo = no.proximo
        if no.proximo is None:
            self.cauda = no.anterior
        else:
            no.proximo.anterior = no.anterior
        no.anterior = no.proximo = None
        self._tamanho -= 1

    def __len__(self):
        return self._tamanho

    def __iter__(self):
        atual = self.cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def reverso(self):
        atual = self.cauda
        while atual is not None:
            yield atual.valor
            atual = atual.anterior

    def __repr__(self):
        return "ListaDupla(" + " <-> ".join(map(str, self)) + ")"


if __name__ == "__main__":
    lista = ListaDupla()
    for v in (1, 2, 3):
        lista.inserir_fim(v)
    lista.inserir_inicio(0)
    print(lista, "len:", len(lista))
    print("reverso:", list(lista.reverso()))
    print("cabeca:", lista.cabeca.valor, "| cauda:", lista.cauda.valor)

    lista.remover_no(lista.cabeca.proximo)
    print("remover_no (meio)   ->", lista, "len:", len(lista))
    lista.remover_no(lista.cabeca)
    print("remover_no (cabeça) ->", lista, "len:", len(lista))
    lista.remover_no(lista.cauda)
    print("remover_no (cauda)  ->", lista, "len:", len(lista))
    lista.remover_no(lista.cabeca)
    print("remover_no (último) ->", lista, "len:", len(lista))
    print("cabeca:", lista.cabeca, "| cauda:", lista.cauda)
