from bubble import bubble_sort
from selection_insertion import selection_sort, insertion_sort
from merge import merge_sort
from quick_pivo import quicksort


class Reg:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __lt__(self, o):
        return self.idade < o.idade

    def __gt__(self, o):
        return self.idade > o.idade

    def __le__(self, o):
        return self.idade <= o.idade

    def __repr__(self):
        return f"{self.nome}{self.idade}"


dados = [Reg("Ana", 30), Reg("Bia", 25), Reg("Caio", 30),
         Reg("Dani", 25), Reg("Edu", 30)]
esperado = ["Bia", "Dani", "Ana", "Caio", "Edu"]


def mostrar(nome, lista):
    estavel = [r.nome for r in lista] == esperado
    print(f"{nome}: {lista} | estável: {estavel}")


b = list(dados); bubble_sort(b); mostrar("bubble", b)
s = list(dados); selection_sort(s); mostrar("selection", s)
i = list(dados); insertion_sort(i); mostrar("insertion", i)
m, _ = merge_sort(dados); mostrar("merge", m)
q = list(dados); quicksort(q, "ultimo"); mostrar("quick", q)
p = sorted(dados, key=lambda r: r.idade); mostrar("sorted", p)
