# Módulo 5 — Módulo `collections`

Currículo 16 (Estruturas de dados). Módulo isolado do `sistema-bancario`.

## O que foi feito

Seis passos práticos, cada um em um arquivo:

1. `deque_basico.py`: operações nas duas pontas e `IndexError` em deque vazio.
2. `deque_custo.py`: `insert(0)` da lista vs `appendleft` do deque, com `timeit`.
3. `counter_basico.py`: contagem, `most_common`, `update`, `+` e `-`.
4. `defaultdict_basico.py`: valor padrão, inserção ao acessar, comparação com `dict` e `Counter`.
5. `namedtuple_basico.py`: campos nomeados, imutabilidade, `_replace`, `_asdict`, uso como chave.
6. `chainmap_basico.py`: busca em camadas, escrita só no primeiro dict, `new_child`, visão sem cópia.

## O que foi visto no módulo

- `deque`: inserção e remoção nas duas pontas em O(1).
- `Counter`: dict especializado em contagem; chave ausente vale 0 e não é inserida.
- `defaultdict`: cria o valor com a `default_factory` e insere a chave ao acessar.
- `namedtuple`: tupla com campos nomeados, imutável e hashable.
- `ChainMap`: várias camadas de dicts numa visão só; leitura percorre em ordem, escrita vai pro primeiro.

## O que foi aprendido

- Com n=80000 inserções no início, o `deque` levou 0.0204s contra 3.3145s da lista (~160x mais rápido): a lista cresce ~4x por dobra de n (O(n²) no total), o deque ~2x (O(n)).
- Acessar chave ausente se comporta de três jeitos: `dict` dá `KeyError`, `Counter` dá `0` sem inserir, `defaultdict` cria e insere.
- No `Counter`, `-` descarta contagens que ficam em zero ou negativas (`Counter("aab") - Counter("abb")` deu `Counter({'a': 1})`).
- `namedtuple` não se altera (`AttributeError`); `_replace` devolve um objeto novo.
- `ChainMap` é uma visão: mudar o dict original (`padrao["tamanho"] = 99`) apareceu no `cfg`; escrever e apagar só mexem no primeiro dict.
