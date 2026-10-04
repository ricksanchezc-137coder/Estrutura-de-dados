print(hash(42), hash(-1), hash(3.0))
print(hash("python"))
print(hash((1, 2, 3)))

try:
    hash([1, 2, 3])
except TypeError as e:
    print("lista:", e)
