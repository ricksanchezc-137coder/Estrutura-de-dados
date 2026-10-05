from functools import cache


@cache
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)


for n in (100, 400, 500, 900, 1000, 5000):
    fib_cache.cache_clear()
    try:
        resultado = fib_cache(n)
        print(f"fib({n}): ok, {len(str(resultado))} dígitos")
    except RecursionError as erro:
        print(f"fib({n}): {type(erro).__name__}: {erro}")
