# Módulo 12 — Grafos (lista e matriz de adjacência)

Resumo de aula do Módulo 12 do Currículo 16 (Estruturas de dados).

## O que foi feito

Sete passos, cada um em um arquivo desta pasta:

1. `lista_basica.py`: grafo A-B, A-C, B-D, C-D, D-E como dict de listas (5 vértices, 5 arestas, grau de D = 3).
2. `matriz_basica.py`: o mesmo grafo como matriz 5×5 (simétrica, mesmas 5 arestas).
3. `custo_espaco.py`: espaço e tempo de montagem num grafo esparso. Lista: 1000 → 8000 entradas; matriz: 62500 → 4000000 células (n de 250 a 2000).
4. `custo_operacoes.py`: teste de aresta e listagem de vizinhos num grafo em estrela. Com n=2000, aresta na lista ~253x mais lenta que na matriz; vizinhos na matriz ~414x mais lentos que na lista.
5. `grafo_lista.py`: classe `GrafoLista` (dict de dicts, direcionado ou não, com peso e erro em laço).
6. `dict_vs_lista.py`: teste de aresta com dict ficou constante (~0,63 µs) contra 49 → 3215 µs na lista (n de 1000 a 64000).
7. `grafo_matriz.py` e `equivalencia.py`: classe `GrafoMatriz` com a mesma interface e teste aleatório com 0 divergências nas 6 execuções.

## O que foi visto no módulo

- O que é um grafo: vértices e arestas; direcionado, ponderado, grau, caminho, ciclo, conexo, esparso e denso.
- Lista de adjacência: espaço O(V + E), vizinhos em O(grau), teste de aresta em O(grau) (com lista de vizinhos).
- Matriz de adjacência: espaço O(V²), teste de aresta em O(1), vizinhos em O(V); simétrica no não direcionado.
- Dict de vizinhos no lugar de lista: teste de aresta em O(1) médio e peso guardado junto, mas `grau_entrada` precisa varrer todos os vértices.
- Diferença entre grafo direcionado e não direcionado ao adicionar e remover arestas, e por que laços foram recusados.

## O que foi aprendido

- A escolha entre lista e matriz é uma troca: a lista economiza memória e percorre vizinhos rápido; a matriz testa aresta rápido, mas gasta V² mesmo quase vazia.
- Medir confirmou a teoria nos dois lados (espaço e operações), em vez de aceitar só a tabela de complexidades.
- Trocar a lista de vizinhos por um dict (ideia do Módulo 3) deixou o teste de aresta constante sem sair da lista de adjacência.
- Nem toda medição saiu limpa (montagem da matriz ~3x por dobra, cópia de vizinhos irregular); isso foi registrado como observação, sem explicação confirmada.
- Um teste aleatório sem divergências é evidência de equivalência entre `GrafoLista` e `GrafoMatriz`, não prova.

