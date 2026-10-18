vertices = ["A", "B", "C", "D", "E"]
indice = {v: i for i, v in enumerate(vertices)}
arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]

n = len(vertices)
matriz = [[0] * n for _ in range(n)]
for u, v in arestas:
    matriz[indice[u]][indice[v]] = 1
    matriz[indice[v]][indice[u]] = 1

print("   ", " ".join(vertices))
for v, linha in zip(vertices, matriz):
    print(v, " ", " ".join(map(str, linha)))

simetrica = all(matriz[i][j] == matriz[j][i] for i in range(n) for j in range(n))
print("simetrica:", simetrica)
print("B-D existe:", matriz[indice["B"]][indice["D"]] == 1)
print("A-E existe:", matriz[indice["A"]][indice["E"]] == 1)
print("grau de D:", sum(matriz[indice["D"]]))
print("vizinhos de D:", [vertices[j] for j in range(n) if matriz[indice["D"]][j]])
print("arestas:", sum(map(sum, matriz)) // 2)
