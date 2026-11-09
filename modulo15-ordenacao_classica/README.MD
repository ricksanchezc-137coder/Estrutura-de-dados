# Módulo 15 — Algoritmos de ordenação clássicos

## O que foi feito

| Arquivo | O que faz |
|---|---|
| `bubble.py` | bubble sort com flag `trocou` e contador de comparações |
| `selection_insertion.py` | selection sort e insertion sort com contador |
| `merge.py` | merge sort recursivo, devolve lista nova e comparações |
| `quick.py` | quicksort in-place com pivô no último elemento |
| `quick_escala.py` | quicksort medido em escala: aleatória, ordenada e limite de recursão |
| `quick_pivo.py` | quicksort com pivô `ultimo`, `mediana3` e `aleatorio` |
| `estabilidade.py` | teste de estabilidade de todos os algoritmos |
| `tempo.py` | tempo real de todos, incluindo `heapq` e `sorted()` |

## O que foi visto no módulo

- Complexidade, estabilidade e uso de memória de bubble, selection, insertion, merge, quicksort e heapsort.
- Melhor, médio e pior caso: quando um algoritmo se adapta à entrada (bubble com flag, insertion) e quando não (selection, merge).
- Pior caso do quicksort com pivô no extremo, e como pivô aleatório e mediana de três ajudam.
- Estabilidade: quem mantém a ordem dos empates e por quê.
- Timsort, usado por `sorted()` e `list.sort()`.

## O que foi aprendido

- Os O(n²) dobram o n e o tempo vai a ~4x; os O(n log n) só ~dobram. Em n=4000, o bubble levou 4.78 s e o merge 0.039 s.
- Com pivô no último elemento, o quicksort em lista ordenada faz n(n−1)/2 comparações e estoura a recursão em n=1000 (ok em n=900).
- Pivô aleatório faz a ordem da entrada deixar de importar; a mediana de três resolveu a ordenada, mas gastou mais na invertida.
- Estáveis nos testes: bubble, insertion, merge e `sorted`; instáveis: selection e quicksort. `estável: True` num teste não prova estabilidade.
- Na prática, usar `sorted()` / `list.sort()`: em n=100000 foi ~12 a 14x mais rápido que meu merge e quick (Timsort + implementação em C), e ~24x mais rápido numa lista já ordenada.
- Pendente: investigar por que a mediana de três gastou mais comparações na lista invertida.
