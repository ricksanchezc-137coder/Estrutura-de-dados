import sys

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

for n in (0, 1, 5, 10):
    print(f"fatorial({n}) = {fatorial(n)}")
print("limite de recursao:", sys.getrecursionlimit())
