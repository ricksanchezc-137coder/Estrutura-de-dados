from functools import cache

chamadas = 0

def fib_ingenuo(n):
    global chamadas
    chamadas += 1
    if n < 2:
        return n
    return fib_ingenuo(n - 1) + fib_ingenuo(n - 2)

@cache
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)

for n in (10, 20, 25):
    chamadas = 0
    fib_cache.cache_clear()
    r1 = fib_ingenuo(n)
    r2 = fib_cache(n)
    print(f"n={n}: resultado={r1} | iguais={r1 == r2} | chamadas sem cache={chamadas}")
    print(" ", fib_cache.cache_info())
