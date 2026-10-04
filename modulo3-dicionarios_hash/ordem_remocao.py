d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3
print(list(d))

d["a"] = 10
print(list(d))

del d["a"]
d["a"] = 1
print(list(d))

try:
    for chave in d:
        if chave == "b":
            del d[chave]
except RuntimeError as e:
    print("erro:", e)
