import timeit
from collections import deque

def lista_insert(n):
    l = []
    for i in range(n):
        l.insert(0, i)

def deque_appendleft(n):
    d = deque()
    for i in range(n):
        d.appendleft(i)

for n in (10000, 20000, 40000, 80000):
    t_l = min(timeit.repeat(lambda: lista_insert(n), number=1, repeat=3))
    t_d = min(timeit.repeat(lambda: deque_appendleft(n), number=1, repeat=3))
    print(f"n={n}: lista {t_l:.4f}s | deque {t_d:.4f}s")
