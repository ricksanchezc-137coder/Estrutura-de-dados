from functools import cache, lru_cache


@cache
def soma(lista):
    return sum(lista)


try:
    soma([1, 2, 3])
except TypeError as erro:
    print(f"lista: {type(erro).__name__}: {erro}")

print("tupla:", soma((1, 2, 3)))
print("tupla de novo:", soma((1, 2, 3)))
print(soma.cache_info())


@lru_cache(maxsize=3)
def quadrado(n):
    return n * n


for n in (1, 2, 3, 4, 1):
    quadrado(n)
    print(f"quadrado({n}) -> {quadrado.cache_info()}")
