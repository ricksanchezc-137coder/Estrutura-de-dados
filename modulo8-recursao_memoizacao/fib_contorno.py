from functools import cache


@cache
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)


def fib_aquecido(n):
    for i in range(n + 1):
        fib_cache(i)
    return fib_cache(n)


def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


for n in (1000, 5000):
    fib_cache.cache_clear()
    r1 = fib_aquecido(n)
    r2 = fib_iter(n)
    print(f"fib({n}): {len(str(r1))} dígitos | iguais={r1 == r2}")
    print("  ", fib_cache.cache_info())
