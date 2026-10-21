# Módulo 14 — Busca binária e bisect

Resumo de aula do Módulo 14 do Currículo 16 (Estruturas de dados).

## O que foi feito

Sete passos, cada um num arquivo da pasta:

1. `busca_binaria.py` — busca binária escrita à mão (início, fim, meio); devolve `-1` se o alvo não existe.
2. `bisect_basico.py` — `bisect_left`, `bisect_right`, `insort`, contagem de repetidos e função `existe`.
3. `custo_busca.py` — `in` vs busca própria vs `bisect` com n de 10 mil a 1 milhão.
4. `insort_custo.py` — n chamadas de `insort` vs montar a lista e ordenar uma vez com `sort`.
5. `aplicacoes.py` — faixas de nota, busca por intervalo e `key=` em registros.
6. `pela_resposta.py` — busca binária pela resposta (raiz quadrada inteira), comparada com `math.isqrt`.
7. `erros_classicos.py` — três versões erradas da busca (loop infinito, off-by-one, lista fora de ordem).

## O que foi visto no módulo

- Busca binária: só vale em lista ordenada, descarta metade a cada passo, custo O(log n).
- Invariante: se o alvo existe, está dentro de `[inicio, fim]`.
- `bisect_left` (posição mais à esquerda) e `bisect_right` (depois dos iguais); `insort` insere mantendo a ordem.
- `insort` é O(n), porque inserir no meio da lista desloca os elementos.
- `key=` no `bisect` (Python 3.10+).
- Busca binária pela resposta: serve para qualquer condição monotônica, sem lista.
- Os três erros clássicos e como testar bordas.

## O que foi aprendido

- Medindo: `in` cresceu ~10x a cada 10x de n; busca própria e `bisect` quase não cresceram. Com 1 milhão de itens, o `in` levou 4,95s e o `bisect` 0,000107s.
- 80 mil `insort` levaram 1,82s e `sort` uma vez levou 0,053s (~34x): `insort` serve para poucas inserções, não para montar a lista.
- O `bisect` ficou ~9 a 10x mais rápido que a busca própria; a causa não foi verificada.
- Busca por intervalo com `bisect_left` + `bisect_right` faz em lista ordenada o que a BST fez no Módulo 10.
- Uma busca binária errada pode não dar erro nenhum: o off-by-one só falha nas bordas e a lista fora de ordem devolve `-1` em silêncio. Por isso: testar primeiro, último, ausente, lista vazia e um elemento.
