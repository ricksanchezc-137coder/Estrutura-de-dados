# modulo4-sets_frozensets/frozenset.py

# 1. Criação e tipo
fs = frozenset([1, 2, 3, 2])
print("1)", fs, len(fs), type(fs))

# 2. Imutável: não tem add/remove
try:
    fs.add(4)
except AttributeError as e:
    print("2) AttributeError:", e)

# 3. Operações misturando set e frozenset
a = frozenset({1, 2, 3})
b = {3, 4}
print("3)", a | b, type(a | b))
print("  ", b | a, type(b | a))

# 4. frozenset é hashable: pode ser elemento de set e chave de dict
grupos = {frozenset({1, 2}), frozenset({2, 1}), frozenset({3})}
print("4)", grupos, len(grupos))
d = {frozenset({"a", "b"}): "par"}
print("  ", d[frozenset({"b", "a"})])
print("  ", hash(frozenset({1, 2})) == hash(frozenset({2, 1})))

# 5. Igualdade entre set e frozenset
print("5)", {1, 2} == frozenset({1, 2}))
