from collections import Counter

c = Counter("banana")
print(c)
print(c["a"], c["z"])
print(len(c))

print(c.most_common(2))

c.update("abacaxi")

print(c)

print(Counter([1, 1, 2]) + Counter([1, 3]))
print(Counter("aab") - Counter("abb"))
print(isinstance(c, dict))
