# Módulo 9 — Árvores binárias e travessias

Currículo 16 (Estruturas de dados). Módulo isolado do `sistema-bancario`.

## O que foi feito

Seis passos práticos, cada um num arquivo:

1. `no_arvore.py`: classe `No` e árvore montada na mão (raiz 1, filhos 2 e 3, netos 4 e 5)
2. `travessias_dfs.py`: pré-ordem, em-ordem e pós-ordem recursivas
- Resultados: `[1, 2, 4, 5, 3]`, `[4, 2, 5, 1, 3]` e `[4, 5, 2, 3, 1]`
3. `travessias_bfs.py`: travessia por nível com `deque`
- Resultados: `[1, 2, 3, 4, 5]` e agrupado `[[1], [2, 3], [4, 5]]`
4. `propriedades.py`: contar nós, contar folhas e altura
- No exemplo: 5 nós, 3 folhas, altura 2; árvore vazia com altura -1
5. `recursao_arvore.py`: DFS iterativa com pilha
- Numa árvore degenerada, a recursiva deu `RecursionError` em n=1000 e n=5000; a iterativa passou nos dois
6. `equilibrada.py`: árvore equilibrada a partir de lista ordenada
- Alturas: n=1000 → 9, n=10000 → 13, n=100000 → 16, n=1000000 → 19

## O que foi visto no módulo

- Vocabulário: raiz, filhos, folha, subárvore e altura (em arestas)
- Árvore binária: nó com valor e dois ponteiros (`esquerda`, `direita`)
- DFS (pré, em, pós-ordem) e BFS (por nível, com fila)
- Recursão com caso base em `None` e combinação do resultado dos dois filhos
- Árvore equilibrada (altura ≈ log n) vs degenerada (altura = n - 1)
- Limite de recursão do Python (1000) e DFS iterativa com pilha própria
- Construção de árvore equilibrada pegando o elemento do meio, com índices (sem fatiar)
- Ideia da árvore de busca binária: a em-ordem devolve os valores ordenados

## O que foi aprendido

- Cada travessia DFS é a mesma recursão; só muda **onde** o valor do nó entra
- A BFS sai nível por nível porque a fila é FIFO
- Numa árvore degenerada a recursão tem um nível por nó e estoura o limite; a pilha própria contorna isso
- Numa equilibrada, n multiplicado por 1000 só soma ~10 níveis na altura (⌊log₂ n⌋)
- Teste dentro de `if __name__ == "__main__":` permite importar `No` e as funções nos outros arquivos
- Ainda não implementamos busca/inserção em BST; só vimos que a em-ordem sai ordenada
