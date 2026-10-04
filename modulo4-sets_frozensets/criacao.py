a = {1, 2, 2, 3, 3, 3}
print(a)
print(len(a))

vazio1 = {}
vazio2 = set()
print(type(vazio1))
print(type(vazio2))

letras = set("banana")
print(letras)

try:
    a[0]
except TypeError as e:
    print("TypeError:", e)

print(3 in a)
print(10 in a)
