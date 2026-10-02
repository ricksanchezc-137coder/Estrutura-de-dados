import timeit

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

for n in [24, 25, 26, 27, 28]:
    t = min(timeit.repeat(lambda: fib(n), number=1, repeat=3))
    print(f"n={n:>2} {t:.4f}s")
