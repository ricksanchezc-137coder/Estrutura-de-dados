class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def __repr__(self):
        return f"No({self.valor})"


def pre_ordem(no):
    if no is None:
        return []
    return [no.valor] + pre_ordem(no.esquerda) + pre_ordem(no.direita)


def em_ordem(no):
    if no is None:
        return []
    return em_ordem(no.esquerda) + [no.valor] + em_ordem(no.direita)


def pos_ordem(no):
    if no is None:
        return []
    return pos_ordem(no.esquerda) + pos_ordem(no.direita) + [no.valor]


def montar_exemplo():
    raiz = No(1)
    raiz.esquerda = No(2)
    raiz.direita = No(3)
    raiz.esquerda.esquerda = No(4)
    raiz.esquerda.direita = No(5)
    return raiz


if __name__ == "__main__":
    raiz = montar_exemplo()
    print("pre-ordem:", pre_ordem(raiz))
    print("em-ordem:", em_ordem(raiz))
    print("pos-ordem:", pos_ordem(raiz))
    print("vazia:", pre_ordem(None), em_ordem(None), pos_ordem(None))
    print("um no:", pre_ordem(No(7)), em_ordem(No(7)), pos_ordem(No(7)))
