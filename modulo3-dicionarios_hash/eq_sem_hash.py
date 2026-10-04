class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

a = Ponto(1, 2)
b = Ponto(1, 2)
print (a == b)
try:
    {a: "primeiro"}
except TypeError as e:
    print("erro:", e)
