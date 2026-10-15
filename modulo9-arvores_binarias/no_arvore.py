class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def __repr__(self):
        return f"no({self.valor})"

raiz = No(1)
raiz.esquerda = No(2)
raiz.direita = No(3)
raiz.esquerda.esquerda = No(4)
raiz.esquerda.direita = No(5)

print("raiz:", raiz.valor)
print("esquerda da raiz:", raiz.esquerda.valor)
print("direita da raiz:", raiz.direita.valor)
print("filho esq do 2:", raiz.esquerda.esquerda.valor)
print("filho dir do 2:", raiz.esquerda.direita.valor)
print("filho esq do 3:", raiz.direita.esquerda)
folha = raiz.esquerda.esquerda
print("4 e folha:", folha.esquerda is None and folha.direita is None)
print(raiz.esquerda)
