from bisect import bisect_left, bisect_right, insort

a = [10, 20, 20, 20, 30, 40]
for x in [5, 10, 20, 25, 40, 50]:
    print(x, "|left:", bisect_left(a, x), "|right:", bisect_right(a, x))

print("quantidade de 20:", bisect_right(a, 20) - bisect_left(a, 20))

def existe(lista, x):
    i = bisect_left(lista, x)
    return i < len(lista) and lista[i] == x

print(existe(a, 20), existe(a, 25), existe(a, 50), existe([], 1))

b = [10, 30]
insort(b, 20)
insort(b, 5)
insort(b, 30)
insort(b, 99)
print(b)
