# Módulo 2 — Listas e tuplas por dentro

Currículo 16 — Estruturas de dados.

## O que foi feito

Seis scripts, cada um com uma medição:

| Script | O que mede |
|---|---|
| `crescimento.py` | Tamanho da lista (`sys.getsizeof`) a cada `append` |
| `append_tempo.py` | Tempo de `n` appends (n de 100 mil a 800 mil) |
| `insert_inicio.py` | Tempo de `n` inserções no início (n de 10 mil a 80 mil) |
| `fatiamento.py` | Tempo de fatiar: fatia crescendo vs lista crescendo |
| `tupla_memoria.py` | Tamanho de lista (via append), lista (via `list`) e tupla |
| `tupla_concatenar.py` | `id` após `+=` e tempo de construir tupla por concatenação |

## O que foi visto no módulo

- A lista guarda referências e reserva espaço de sobra, então o tamanho cresce em saltos.
- `append` tem custo ~constante; `insert(0, x)` custa proporcional ao tamanho da lista.
- Fatiar custa proporcional ao tamanho da fatia, não ao tamanho da lista original.
- Tupla é imutável: ocupa menos memória e `+=` cria um objeto novo.
- Como medir custo com `timeit` e ler o resultado pela razão ao dobrar `n`.

## O que foi aprendido

- `append`: o tempo total dobrou quando n dobrou (~O(1) por chamada).
- `insert(0, x)`: o tempo total quadruplicou quando n dobrou (O(n) por chamada).
- `lista[:k]`: ~2x por dobra de k, e ~8 µs constantes quando k fixo e a lista cresce.
- Tupla: 48 + 8·n bytes nos casos medidos, sempre menor que a lista.
- Construir tupla por concatenação foi muito mais lento que `append` (40 mil concatenações: 13.5950s; 800 mil appends: 0.2291s).
- Ficou em aberto: por que as razões na concatenação de tupla passaram de 4x.
