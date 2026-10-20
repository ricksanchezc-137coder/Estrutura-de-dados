# Módulo 13 — Busca em grafos: BFS e DFS

Resumo de aula do Módulo 13 do Currículo 16 (Estruturas de dados).

## O que foi feito

Oito passos, cada um em um arquivo desta pasta:

1. `bfs.py` — BFS com fila; `bfs de E` deu `E, D, B, C, A`, e o vértice F isolado não apareceu na busca a partir de A.
2. `dfs.py` — DFS recursiva e iterativa; as duas deram a mesma ordem (`A, B, D, C, E` a partir de A).
3. `menor_caminho.py` — menor caminho com BFS e dicionário `pai`; `A -> E` deu `A, B, D, E` e `A -> F` deu `None`.
4. `dfs_vs_bfs.py` — no anel, de A até E a BFS achou 1 aresta e a DFS 4.
5. `componentes.py` — componentes conectados (1, 2 e 3 componentes nos testes).
6. `ciclo.py` — detecção de ciclo em grafo não direcionado, inclusive com o ciclo só no segundo componente.
7. `custo.py` — tempo dobrou a cada dobra de n (O(V + E)); a DFS recursiva quebrou com `RecursionError` em n=1000, a iterativa visitou 5000 vértices.
8. `labirinto.py` — BFS numa grade: menor caminho de 15 passos de `S` até `E`.

## O que foi visto no módulo

- BFS (fila) e DFS (pilha ou recursão), e por que um grafo precisa de `visitados`.
- BFS marca como visitado ao enfileirar; a DFS iterativa marca ao desempilhar.
- Dicionário `pai` para reconstruir o caminho.
- Componentes conectados e detecção de ciclo (ignorando o pai).
- Custo O(V + E) com lista de adjacência.
- Limite de recursão da DFS recursiva.
- Grade tratada como grafo, com vizinhos calculados na hora.

## O que foi aprendido

- A BFS dá o menor número de arestas; a DFS acha um caminho, não necessariamente o menor.
- Quando há empate de caminhos, a ordem de exploração dos vizinhos decide qual aparece.
- A DFS recursiva tem o mesmo limite de 1000 dos Módulos 8 e 9; a versão com pilha própria contorna.
- Um laço externo sobre todos os vértices é necessário para cobrir os componentes desconectados.
- Em grafo não direcionado, um vizinho já visitado só indica ciclo se não for o pai.
