# Módulo 4 — Sets e frozenset

Currículo 16 — Estruturas de dados.

## O que foi feito

Seis scripts, um por passo, cada um com saída conferida no terminal:

- `criacao.py`: criação de sets, duplicatas, `{}` vs `set()`, ausência de índice e pertencimento com `in`.
- `operacoes.py`: união, interseção, diferença, diferença simétrica, subconjunto/superconjunto, `isdisjoint` e a diferença entre operador e método.
- `custo.py`: medição com `timeit` de `add` (total linear), interseção entre set pequeno e set grande (tempo constante em relação ao set grande) e `remove` vs `discard`.
- `hashable.py`: o que pode ou não ser elemento de set (`list`, `set`, tupla com lista dentro) e por que `{1, 1.0, True}` vira `{1}`.
- `frozenset.py`: imutabilidade, tipo do resultado em operações mistas, `frozenset` como elemento de set e chave de dict, igualdade com `set`.
- `deduplicar.py`: três formas de remover duplicatas (lista com `not in`, `set`, `dict.fromkeys`), com ordem do resultado e tempos medidos.

## O que foi visto no módulo

- Set como coleção sem duplicatas, sem índice e sem ordem garantida, baseada em tabela hash (parecida com a do dict).
- Criação (`{...}`, `set(iterável)`, `set()`) e a armadilha do `{}`.
- Operações de conjunto e seus métodos equivalentes.
- `add`, `remove`, `discard`, `pop` e `clear`.
- Custo: `in`/`add`/`remove`/`discard` O(1) em média; união O(len(s1) + len(s2)); interseção O(min(len(s1), len(s2))).
- Requisito de elementos hashable e a relação com `__hash__`/`__eq__` do Módulo 3.
- `frozenset`: set imutável e hashable.
- Deduplicação e o impacto de usar lista (O(n²)) contra set/dict (O(n)).

## O que foi aprendido

- A ordem de um set pode mudar entre execuções (hash de `str` muda), então nunca se deve depender dela.
- `a[0]` em set dá `TypeError`: não existe posição acessível.
- Operador (`|`, `&`, `-`, `^`) exige set dos dois lados; o método aceita qualquer iterável.
- A interseção não depende do tamanho do set grande: medi ~86 ms (1000 chamadas) pra todos os tamanhos de 100 mil a 800 mil.
- `discard` ignora elemento ausente; `remove` levanta `KeyError`.
- Uma tupla só é hashable se tudo dentro dela for; `(1, [2, 3])` não entra num set.
- `1`, `1.0` e `True` são o mesmo elemento pra um set.
- Em `set | frozenset`, o tipo do resultado segue o primeiro operando.
- Deduplicar com lista + `not in` ficou ~4x mais lento a cada dobra de n; com n = 8000, cerca de 1600x mais lento que com set.
- `set(xs)` não preserva ordem; `dict.fromkeys(xs)` preserva a ordem de inserção.
