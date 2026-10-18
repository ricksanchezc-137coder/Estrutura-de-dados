# Módulo 11 — Heaps e heapq

Currículo 16 (Estruturas de dados) · 18/10/2026

## O que foi feito

Sete scripts, um por passo, todos nesta pasta:

1. `heap_basico.py` — pushes, `heap[0]`, pops em sequência e `IndexError` em heap vazio
2. `heapify_regra.py` — função `eh_heap`, `heapify`, índices de pai e filhos, `sort()` sobre um heap
3. `custo_heapify.py` — tempo de n pushes vs `heapify` (100 mil a 800 mil itens)
4. `comparacoes.py` — contagem de comparações com uma classe `Contado`
5. `pior_caso.py` — pushes em ordem aleatória, crescente e decrescente
6. `fila_prioridade.py` — max-heap com negativos, tuplas `(prioridade, tarefa)`, erro de empate e desempate com contador
7. `heaps_extras.py` — `nsmallest`, `nlargest` (com `key`), `merge` e heapsort

## O que foi visto no módulo

- Heap é uma árvore binária completa guardada numa lista: filhos de `i` em `2i+1` e `2i+2`, pai em `(i-1)//2`
- O `heapq` é um min-heap: `heap[0]` é sempre o menor
- Heap não é ordenado: só garante pai ≤ filhos
- `heappush` e `heappop` são O(log n) no pior caso; `heapify` é O(n)
- Max-heap guardando valores negativos
- Fila de prioridade com tuplas e contador de desempate
- `nsmallest`, `nlargest`, `merge` e heapsort

## O que foi aprendido

- O `heapify` foi ~2x mais rápido que n pushes em todos os tamanhos testados
- Contar comparações deu resultados mais confiáveis que o cronômetro neste celular: `heapify` ficou em ~1,65 comparações por item (linear) e os pushes aleatórios em ~2,27
- O pior caso do push aparece com entrada decrescente (custo por item cresce com `log2 n`); com entrada crescente o custo é 1 comparação por item
- "n pushes somam O(n log n)" é o limite do pior caso, não o que acontece com dados aleatórios
- Prioridades iguais com objetos sem comparação dão `TypeError`; um contador no meio da tupla resolve e mantém a ordem de inserção nos empates
- O tempo medido não cresceu de forma regular com n e a causa não foi identificada
