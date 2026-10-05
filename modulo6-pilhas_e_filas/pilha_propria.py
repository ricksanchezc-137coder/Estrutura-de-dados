# modulo6-pilhas_e_filas/pilha_propria.py

class Pilha:
    def __init__(self):
        self._itens = []

    def push(self, valor):
        self._itens.append(valor)

    def pop(self):
        if self.esta_vazia():
            raise IndexError("pilha vazia")
        return self._itens.pop()

    def peek(self):
        if self.esta_vazia():
            raise IndexError("pilha vazia")
        return self._itens[-1]

    def esta_vazia(self):
        return len(self._itens) == 0

    def __len__(self):
        return len(self._itens)

    def __repr__(self):
        return f"Pilha({self._itens})"


if __name__ == "__main__":
    p = Pilha()
    for valor in (1, 2, 3):
        p.push(valor)
        print(f"push {valor}: {p}")

    print(f"peek: {p.peek()}, len: {len(p)}")

    while not p.esta_vazia():
        print(f"pop -> {p.pop()}: {p}")

    try:
        p.pop()
    except IndexError as erro:
        print(f"IndexError: {erro}")
