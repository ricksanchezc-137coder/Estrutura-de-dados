import sys
from bisect import bisect, bisect_left, bisect_right, insort

print(sys.version)

cortes = [60, 70, 80, 90]
letras = "FDCBA"

def conceito(nota):
    return letras[bisect(cortes, nota)]

print([conceito(n) for n in [33, 60, 65, 70, 89, 90, 100]])

a = [10, 20, 20, 30, 40, 50, 60]

def intervalo(lista, lo, hi):
    return lista[bisect_left(lista, lo):bisect_right(lista, hi)]

print(intervalo(a, 20, 40), intervalo(a, 25, 35), intervalo(a, 0, 5), intervalo(a, 60, 100))

filmes = [("A", 1950), ("B", 1960), ("C", 1960), ("D", 1975), ("E", 1990)]

def ano(f):
    return f[1]

print(bisect_left(filmes, 1960, key=ano), bisect_right(filmes, 1960, key=ano))
insort(filmes, ("F", 1960), key=ano)
print(filmes)
