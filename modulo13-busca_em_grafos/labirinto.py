from collections import deque

LABIRINTO = [
    "S.#.....",
    ".##.###.",
    "....#...",
    ".####.#.",
    "......#E",
]


def achar(grade, marca):
    for r, linha in enumerate(grade):
        for c, ch in enumerate(linha):
            if ch == marca:
                return (r, c)
    return None


def vizinhos(grade, pos):
    r, c = pos
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grade) and 0 <= nc < len(grade[nr]):
            if grade[nr][nc] != "#":
                yield (nr, nc)


def menor_caminho_grade(grade):
    inicio = achar(grade, "S")
    fim = achar(grade, "E")
    pai = {inicio: None}
    fila = deque([inicio])
    while fila:
        v = fila.popleft()
        if v == fim:
            break
        for w in vizinhos(grade, v):
            if w not in pai:
                pai[w] = v
                fila.append(w)
    if fim not in pai:
        return None
    caminho = []
    v = fim
    while v is not None:
        caminho.append(v)
        v = pai[v]
    caminho.reverse()
    return caminho


def desenhar(grade, caminho):
    linhas = [list(l) for l in grade]
    for r, c in caminho[1:-1]:
        linhas[r][c] = "*"
    return ["".join(l) for l in linhas]


if __name__ == "__main__":
    caminho = menor_caminho_grade(LABIRINTO)
    print("passos:", len(caminho) - 1)
    print("caminho:", caminho)
    for linha in desenhar(LABIRINTO, caminho):
        print(linha)

    print("sem saida:", menor_caminho_grade(["S#E"]))
    caminho2 = menor_caminho_grade(["SE"])
    print("lado a lado:", caminho2, "passos:", len(caminho2) - 1)
