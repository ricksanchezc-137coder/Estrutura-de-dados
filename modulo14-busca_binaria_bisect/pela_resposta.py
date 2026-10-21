import math
from bisect import bisect_left


def primeiro_verdadeiro(lo, hi, cond):
    """Menor x em [lo, hi) com cond(x) True; devolve hi se nenhum."""
    while lo < hi:
        meio = (lo + hi) // 2
        if cond(meio):
            hi = meio
        else:
            lo = meio + 1
    return lo


def raiz_inteira(n):
    return primeiro_verdadeiro(0, n + 2, lambda x: x * x > n) - 1


print([raiz_inteira(n) for n in [0, 1, 2, 3, 4, 15, 16, 17, 99, 100]])
print(all(raiz_inteira(n) == math.isqrt(n) for n in range(5000)))
print(raiz_inteira(10**18), math.isqrt(10**18))
print(raiz_inteira(10**40) == math.isqrt(10**40))

# Experimento: bisect sobre um range, com key devolvendo True/False
print(bisect_left(range(99 + 2), True, key=lambda x: x * x > 99))
