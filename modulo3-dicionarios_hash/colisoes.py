import timeit

class ChaveBoa:
    def __init__(self, v):
        self.v = v

    def __eq__(self, outro):
        return self.v == outro.v

    def __hash__(self):
        return hash(self.v)

class ChaveRuim(ChaveBoa):
    def __hash__(self):
        return 1

def montar(classe, n):
    return {classe(i): i for i in range(n)}

for n in (500, 1000, 2000, 4000):
    t_boa = min(timeit.repeat(lambda: montar(ChaveBoa, n), number=1, repeat=3))
    t_ruim = min(timeit.repeat(lambda: montar(ChaveRuim, n), number=1, repeat=3))
    print(f"n={n}: boa {t_boa:.4f}s | ruim {t_ruim:.4f}s")

