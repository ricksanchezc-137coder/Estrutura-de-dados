class GrafoLista:
    def __init__(self, direcionado=False):
        self.direcionado = direcionado
        self._adj = {}

    def adicionar_vertice(self, v):
        if v not in self._adj:
            self._adj[v] = {}

    def adicionar_aresta(self, u, v, peso=1):
        if u == v:
            raise ValueError("laco (aresta de um vertice nele mesmo) nao permitido")
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        self._adj[u][v] = peso
        if not self.direcionado:
            self._adj[v][u] = peso

    def remover_aresta(self, u, v):
        if u not in self._adj or v not in self._adj[u]:
            return False
        del self._adj[u][v]
        if not self.direcionado:
            del self._adj[v][u]
        return True

    def tem_aresta(self, u, v):
        return u in self._adj and v in self._adj[u]

    def peso(self, u, v):
        return self._adj[u][v]

    def vizinhos(self, u):
        return list(self._adj[u])

    def grau(self, u):
        return len(self._adj[u])

    def grau_entrada(self, u):
        return sum(1 for viz in self._adj.values() if u in viz)

    def num_arestas(self):
        total = sum(len(viz) for viz in self._adj.values())
        return total if self.direcionado else total // 2

    def __len__(self):
        return len(self._adj)

    def __repr__(self):
        return f"GrafoLista({self._adj})"


if __name__ == "__main__":
    g = GrafoLista()
    for u, v in [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]:
        g.adicionar_aresta(u, v)
    print(g)
    print("vertices:", len(g), "| arestas:", g.num_arestas())
    print("vizinhos de D:", g.vizinhos("D"), "| grau:", g.grau("D"))
    print("B-D:", g.tem_aresta("B", "D"), "| D-B:", g.tem_aresta("D", "B"),
          "| A-E:", g.tem_aresta("A", "E"))
    print("remover B-D:", g.remover_aresta("B", "D"), "->",
          g.tem_aresta("B", "D"), g.tem_aresta("D", "B"), g.num_arestas())
    print("remover B-D de novo:", g.remover_aresta("B", "D"))

    d = GrafoLista(direcionado=True)
    d.adicionar_aresta("X", "Y", peso=5)
    d.adicionar_aresta("Y", "Z", peso=2)
    d.adicionar_aresta("Z", "X", peso=7)
    print(d)
    print("X->Y:", d.tem_aresta("X", "Y"), "| Y->X:", d.tem_aresta("Y", "X"))
    print("peso X->Y:", d.peso("X", "Y"))
    print("grau saida X:", d.grau("X"), "| grau entrada X:", d.grau_entrada("X"))
    print("arestas:", d.num_arestas())

    try:
        g.adicionar_aresta("A", "A")
    except ValueError as e:
        print("erro:", e)
