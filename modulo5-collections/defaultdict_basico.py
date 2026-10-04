from collections import defaultdict

d = defaultdict(list)
print(d["a"])
print(d)
print(len(d))

d["x"].append(1)
d["x"].append(2)
d["y"].append(3)
print(d)

cont = defaultdict(int)
for ch in "banana":
    cont[ch] += 1
print(cont)

print(d.default_factory)

comum = {}
try:
    comum["a"]
except KeyError as e:
    print("KeyError", e)

print("z" in d)
d["z"]
print("z" in d)
print(isinstance(d, dict))
