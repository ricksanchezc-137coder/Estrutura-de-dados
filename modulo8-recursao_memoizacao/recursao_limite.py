import sys

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

print("limite:", sys.getrecursionlimit())

for n in (500, 900, 1000, 5000):
    try:
        resultado = fatorial(n)
        print(f"fatorial({n}): ok  {len(str(resultado))} digitos")
    except RecursionError as e:
        print(f"fatorial({n}): {type(e).__name__}: {e}")
