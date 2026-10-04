# Módulo 3 — Dicionários e tabelas hash

Currículo 16 (Estruturas de dados).

## O que foi feito

Sete experimentos, todos isolados do `sistema-bancario`:

| Passo | Arquivo | O que mostra |
|---|---|---|
| 1 | `hash_basico.py` | hash de int, str, tupla e lista |
| 2 | `eq_sem_hash.py` | classe com só `__eq__` não serve como chave |
| 3 | `eq_com_hash.py` | `__eq__` + `__hash__` coerentes funcionam em dict e set |
| 4 | `colisoes.py` | hash constante deixa a montagem do dict O(n²) |
| 5 | `chave_mutavel.py` | mudar a chave depois de inserir a torna inalcançável |
| 6 | `crescimento_dict.py` | o tamanho do dict muda em `len` 1, 6, 11, 22, 43 |
| 7 | `ordem_remocao.py` | ordem de inserção e `RuntimeError` ao remover no `for` |

## O que foi visto no módulo

- O que é o hash e a regra central: objetos iguais têm o mesmo hash.
- Hash de `str` é randomizado por execução; hash de `int` e de tupla de ints não.
- Por que `list`, `dict` e `set` não são hasheáveis.
- Como `__eq__` e `__hash__` trabalham juntos, e o que acontece quando só um existe.
- Colisões e o custo delas no dict.
- Crescimento (redimensionamento) da tabela e inserção O(1) amortizada.
- Ordem de inserção dos dicts e a regra de não mudar o tamanho durante a iteração.

## O que foi aprendido

- Com hash constante, montar o dict com `n=4000` levou 2.8659 s contra 0.0051 s com hash bom, e o tempo quadruplicava a cada dobra de `n`.
- Se um campo usado no `__hash__` muda depois da inserção, o item continua no dict mas não é mais encontrado.
- Definir `__eq__` sem `__hash__` deixa a classe não hasheável.
- Atualizar o valor de uma chave não muda a posição dela; remover e reinserir manda a chave pro fim.
- Pra remover itens durante um laço, iterar sobre uma cópia (`list(d)`).
