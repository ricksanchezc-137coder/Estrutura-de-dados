import timeit
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)

for n in [28, 50, 100, 200, 400]:
    t = min(timeit.repeat(
        lambda: (fib_cache.cache_clear(), fib_cache(n)),
        number=1, repeat=5))
    print(f"n={n:>3} {t:.6f}s")
