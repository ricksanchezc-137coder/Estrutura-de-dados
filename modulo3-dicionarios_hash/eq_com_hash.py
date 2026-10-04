class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

    def __hash__(self):
        return hash((self.x, self.y))

a = Ponto(1, 2)
b = Ponto(1, 2)
print(hash(a) == hash(b))

d = {a: "primeiro"}
d[b] = "segundo"
print(len(d), d[a])

print(len({Ponto(1, 2), Ponto(1, 2), Ponto(3, 4)}))
