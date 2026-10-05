class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaSimples:
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    def inserir_inicio(self, valor):
        no = No(valor)
        no.proximo = self.cabeca
        self.cabeca = no
        self._tamanho += 1

    def inserir_fim(self, valor):
        no = No(valor)
        if self.cabeca is None:
            self.cabeca = no
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = no
        self._tamanho += 1

    def __len__(self):
        return self._tamanho

    def __iter__(self):
        atual = self.cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __repr__(self):
        return "ListaSimples(" + " -> ".join(map(str, self)) + ")"

    def __contains__(self, valor):
        atual = self.cabeca
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False

    def remover(self, valor):
        anterior = None
        atual = self.cabeca
        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self._tamanho -= 1
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def inverter(self):
        anterior = None
        atual = self.cabeca
        while atual is not None:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.cabeca = anterior

if __name__ == "__main__":
    lista = ListaSimples()
    print(lista, len(lista))
    for v in (1, 2, 3):
        lista.inserir_inicio(v)
        print("inserir_inicio", v, "->", lista)
    print("len:", len(lista))
    print("lista:", list(lista))
    print("cabeca.valor:", lista.cabeca.valor)
    print("cabeca.proximo.valor:", lista.cabeca.proximo.valor)
    print("fim:", lista.cabeca.proximo.proximo.proximo)
