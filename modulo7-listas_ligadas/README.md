# Módulo 7 — Listas ligadas (simples e dupla)

Currículo 16 — Estruturas de dados.

## O que foi feito

| Arquivo | O que faz |
|---|---|
| `lista_simples.py` | `No` e `ListaSimples`: `inserir_inicio`, `inserir_fim`, `__contains__`, `remover`, `inverter`, `__len__`, `__iter__`, `__repr__` |
| `custo_insercao.py` | tempo de `n` inserções no início vs no fim da simples |
| `remover.py` | teste de buscar e remover (cabeça, meio, fim, inexistente, lista vazia) |
| `lista_dupla.py` | `NoDuplo` e `ListaDupla` com `cauda`, `inserir_inicio`, `inserir_fim`, `remover_no`, `reverso` |
| `custo_dupla.py` | simples vs dupla no `inserir_fim`; `list` vs ligada no acesso ao meio |
| `inverter.py` | teste do `inverter` (lista normal, um elemento, vazia, inverter duas vezes) |
| `ciclo.py` | `tem_ciclo` com tartaruga e lebre |

Medições principais:

- `inserir_fim` na simples: ~4x por dobra de `n` (n=8000: 1.9346s), contra ~2x no início (0.0090s).
- Dupla com cauda no `inserir_fim`: n=8000 em 0.0076s, contra 1.8704s na simples.
- Acesso ao meio com n=80000: `list` 0.000014s, ligada 0.610309s (100 acessos).

## O que foi visto no módulo

- Lista ligada: nós com valor e referência para o próximo; a lista guarda só a cabeça (e a cauda, na dupla).
- Simples (só `proximo`) e dupla (`anterior` e `proximo`).
- Custos: inserir no início O(1); inserir no fim O(n) sem cauda e O(1) com cauda; remover um nó em mãos O(n) na simples e O(1) na dupla; acesso por índice O(n); buscar O(n).
- Diferença para a `list`: array contíguo com acesso O(1) por índice, contra nós espalhados na memória.
- Religar ponteiros: a ordem importa e os casos de borda (vazia, um elemento, cabeça, cauda) precisam ser tratados.
- Inverter com três ponteiros e detectar ciclo com tartaruga e lebre (Floyd), ambos O(n) em tempo e O(1) em memória extra.
- O `deque` do CPython é uma lista duplamente ligada de blocos de tamanho fixo.

## O que foi aprendido

- Medir confirma a teoria: dobrar `n` multiplica o tempo por ~2 (O(n)) ou ~4 (O(n²)) ou nada (O(1)).
- O ganho da lista dupla é poder remover um nó que já se tem em mãos sem percorrer a lista.
- Guardar o `proximo` antes de sobrescrever o ponteiro evita perder o resto da lista.
- Ao remover o último nó da dupla, `cabeca` e `cauda` precisam virar `None` juntos.
- Lista com ciclo faz a iteração normal travar, então é preciso um algoritmo próprio para detectar.
- Lista ligada ganha em inserir e remover nas pontas; para acesso por posição, a `list` é muito melhor.
