# Módulo 1 — Complexidade e Big-O

Currículo 16 (Estruturas de dados) · 02/10/2026

## O que foi feito

Oito scripts, todos medindo o tempo com `timeit.repeat` + `min` e olhando a razão entre os tempos ao dobrar o n:

| Arquivo | O que mediu | Resultado |
|---|---|---|
| `linear.py` | soma de lista | tempo dobra com n (O(n)) |
| `quadratico.py` | duplicata com dois laços | tempo quadruplica com n dobrado (O(n²)) |
| `linear_set.py` | duplicata com `set` | O(n); mais de 4000x mais rápido que o quadrático em n=4000 |
| `buscar.py` | `in` em lista vs set | lista O(n), set ~constante (O(1)) |
| `binaria.py` | `bisect_left` | n 100x maior, tempo ~16% maior (O(log n)) |
| `ordenacao.py` | `sorted` | ~2,4x por dobra de n (O(n log n)) |
| `exponencial.py` | `fib` recursivo | ~1,6x a cada +1 em n (exponencial) |
| `memorizacao.py` | `fib` com `lru_cache` | de exponencial pra linear; ~5.600x mais rápido em n=28 |

## O que foi visto no módulo

- Big-O descreve a taxa de crescimento do custo conforme o tamanho da entrada, não segundos.
- As classes O(1), O(log n), O(n), O(n log n), O(n²) e exponencial, e como reconhecê-las dobrando o n.
- Pior caso vs caso médio; os tempos de `set`/`dict` são de caso médio e dependem de um bom hash (fonte: documentação do Python sobre complexidade dos tipos built-in).
- Busca binária (`bisect`) exige lista ordenada.
- Memoização com `functools.lru_cache`.

## O que foi aprendido

- Medir de verdade: apostar antes, rodar, comparar razões em vez de olhar um tempo isolado.
- Trocar a estrutura de dados (lista → set) muda a classe de complexidade e rende diferenças de milhares de vezes.
- Custo fixo de chamada pode esconder o crescimento real (caso do bisect).
- Memoização troca memória por tempo.
- O `fib` recursivo cresce como ~1,618ⁿ; O(2ⁿ) é só um limite superior.
- Alguns resultados ficaram um pouco acima do ideal (2,27x, ~2,4x, 2,3x) e a causa não foi determinada.
