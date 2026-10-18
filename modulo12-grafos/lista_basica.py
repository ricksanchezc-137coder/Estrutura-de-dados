grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}

print("vertices:", list(grafo))
print("vizinhos de D:", grafo["D"])
print("grau de D:", len(grafo["D"]))
print("B-D existe:", "D" in grafo["B"])
print("A-E existe:", "E" in grafo["A"])

arestas = sum(len(v) for v in grafo.values()) // 2
print("arestas:", arestas)
