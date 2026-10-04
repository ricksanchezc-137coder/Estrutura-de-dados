a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a.union(b))

print(a & b)
print(a.intersection(b))

print(a - b)
print(b - a)

print(a ^ b)

print({1, 2} <= a)
print(a >= {1, 2})
print(a.isdisjoint({7, 8}))

print(a.union([10, 11]))
try:
    print(a | [10, 11])
except TypeError as e:
    print("TypeError:", e)

