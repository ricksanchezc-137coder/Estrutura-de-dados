# Módulo 8 — Recursão e memoização (functools.cache)

Currículo 16 (Estruturas de dados) · concluído em 05/10/2026

## O que foi feito

Sete scripts, um por passo:

1. `fatorial.py` — fatorial recursivo com caso base; limite de recursão da máquina: 1000.
2. `recursao_limite.py` — `fatorial(900)` funcionou, `fatorial(1000)` e `fatorial(5000)` deram `RecursionError`.
3. `fib_cache.py` — `fib(25)`: 242785 chamadas sem cache contra 26 misses com `@cache`.
4. `fib_limite.py` — `fib(900)` funcionou com cache, `fib(1000)` e `fib(5000)` deram `RecursionError`.
5. `fib_contorno.py` — aquecendo o cache em ordem crescente, `fib(1000)` e `fib(5000)` funcionaram, com resultado igual ao da versão com laço.
6. `cache_limites.py` — lista como argumento deu `TypeError`; `lru_cache(maxsize=3)` descartou a entrada mais antiga ao encher.
7. `caminhos_grade.py` — grade 10x10: 369511 chamadas sem cache contra 120 misses com cache; grade 100x100 só rodou com cache (10200 misses).

## O que foi visto no módulo

- Recursão: caso base, caso recursivo e pilha de chamadas.
- `RecursionError` e o limite de profundidade (`sys.getrecursionlimit()`).
- Subproblemas repetidos e o custo exponencial do `fib` ingênuo.
- Memoização: guardar o resultado de cada chamada pelos argumentos.
- `functools.cache` e `lru_cache(maxsize=N)`, com `cache_info()` e `cache_clear()`.
- Argumentos hashable como exigência do cache.
- Memoização com dois argumentos (grade).

## O que foi aprendido

- O cache transforma o custo exponencial em custo proporcional ao número de subproblemas distintos (`n+1` no Fibonacci, `n(n+2)` na grade).
- O cache resolve o tempo, mas não a profundidade: `fib(1000)` com `@cache` quebrou no mesmo ponto do fatorial.
- Aquecer o cache em ordem crescente, ou usar um laço, evita o `RecursionError`.
- O cache só aceita argumentos hashable, e `maxsize=None` deixa a memória crescer sem limite.
- `cache_info()` mostra se o cache está funcionando: hits e misses se explicam pela estrutura do problema.
