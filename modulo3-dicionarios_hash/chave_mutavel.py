class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

    def __hash__(self):
        return hash((self.x, self.y))

p = Ponto(1, 2)
d = {p: "achei"}
print(p in d)

p.x = 99
print(p in d)
print(len(d))
print(Ponto(1, 2) in d)
