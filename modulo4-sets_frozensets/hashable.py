# modulo4-sets_frozensets/hashable.py

# 1. list dentro de set
try:
    s = {[1, 2], [3, 4]}
except TypeError as e:
    print("1) TypeError:", e)

# 2. tupla funciona (e duplicata some)
s = {(1, 2), (3, 4), (1, 2)}
print("2)", s, len(s))

# 3. tupla com lista dentro
try:
    s = {(1, [2, 3])}
except TypeError as e:
    print("3) TypeError:", e)

# 4. set dentro de set
try:
    s = {{1, 2}}
except TypeError as e:
    print("4) TypeError:", e)

# 5. 1, 1.0 e True são iguais entre si
print("5)", 1 == 1.0 == True)
print("   hashes:", hash(1), hash(1.0), hash(True))
x = {1, 1.0, True}
print("   set:", x, len(x))
