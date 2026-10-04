from collections import namedtuple

Ponto = namedtuple("Ponto", ["x", "y"])
p = Ponto(1, 2)
print(p)
print(p.x, p.y, p[0], p[1])

x, y = p
print(x, y)
print(isinstance(p, tuple), len(p))
print(p == (1, 2))

try:
    p.x = 10
except AttributeError as e:
    print("AttributeError", e)

q = p._replace(x=10)
print(q, p)
print(p._asdict())
print(Ponto._fields)

d = {p: "ok"}
print(d[Ponto(1, 2)])
