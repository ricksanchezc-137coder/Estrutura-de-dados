class GrafoMatriz:
    def __init__(self, direcionado=False):
        self.direcionado = direcionado
        self._indice = {}
        self._rotulos = []
        self._m = []

    def adicionar_vertice(self, v):
        if v in self._indice:
            return
        self._indice[v] = len(self._rotulos)
        self._rotulos.append(v)
        for linha in self._m:
            linha.append(None)
        self._m.append([None] * len(self._rotulos))

    def adicionar_aresta(self, u, v, peso=1):
        if u == v:
            raise ValueError("laco (aresta de um vertice nele mesmo) nao permitido")
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        i, j = self._indice[u], self._indice[v]
        self._m[i][j] = peso
        if not self.direcionado:
            self._m[j][i] = peso

    def tem_aresta(self, u, v):
        if u not in self._indice or v not in self._indice:
            return False
        return self._m[self._indice[u]][self._indice[v]] is not None

    def remover_aresta(self, u, v):
        if not self.tem_aresta(u, v):
            return False
        i, j = self._indice[u], self._indice[v]
        self._m[i][j] = None
        if not self.direcionado:
            self._m[j][i] = None
        return True

    def peso(self, u, v):
        valor = self._m[self._indice[u]][self._indice[v]]
        if valor is None:
            raise KeyError(v)
        return valor

    def vizinhos(self, u):
        i = self._indice[u]
        return [self._rotulos[j] for j, p in enumerate(self._m[i]) if p is not None]

    def grau(self, u):
        return sum(1 for p in self._m[self._indice[u]] if p is not None)

    def grau_entrada(self, u):
        j = self._indice[u]
        return sum(1 for linha in self._m if linha[j] is not None)

    def num_arestas(self):
        total = sum(1 for linha in self._m for p in linha if p is not None)
        return total if self.direcionado else total // 2

    def __len__(self):
        return len(self._rotulos)

    def __repr__(self):
        return f"GrafoMatriz({self._m})"


if __name__ == "__main__":
    g = GrafoMatriz()
    for u, v in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]:
        g.adicionar_aresta(u, v)
    print(g)
    print("vertices:", len(g), "| arestas:", g.num_arestas())
    print("vizinhos de D:", g.vizinhos("D"), "| grau:", g.grau("D"))
    print("remover B-D:", g.remover_aresta("B", "D"), "->",
          g.tem_aresta("B", "D"), g.tem_aresta("D", "B"), g.num_arestas())
