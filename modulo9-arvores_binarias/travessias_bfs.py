from collections import deque

from travessias_dfs import No, montar_exemplo


def por_nivel(raiz):
    if raiz is None:
        return []
    resultado = []
    fila = deque([raiz])
    while fila:
        no = fila.popleft()
        resultado.append(no.valor)
        if no.esquerda is not None:
            fila.append(no.esquerda)
        if no.direita is not None:
            fila.append(no.direita)
    return resultado


def por_niveis_agrupados(raiz):
    if raiz is None:
        return []
    niveis = []
    fila = deque([raiz])
    while fila:
        tamanho = len(fila)
        nivel = []
        for _ in range(tamanho):
            no = fila.popleft()
            nivel.append(no.valor)
            if no.esquerda is not None:
                fila.append(no.esquerda)
            if no.direita is not None:
                fila.append(no.direita)
        niveis.append(nivel)
    return niveis


if __name__ == "__main__":
    raiz = montar_exemplo()
    print("por nivel:", por_nivel(raiz))
    print("agrupado:", por_niveis_agrupados(raiz))
    print("vazia:", por_nivel(None), por_niveis_agrupados(None))
    print("um no:", por_nivel(No(7)), por_niveis_agrupados(No(7)))
