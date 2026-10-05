# Módulo 6 — Pilhas e filas (implementação própria, deque vs list)

Currículo 16 — Estruturas de dados.

## O que foi feito

Seis exercícios em Python, cada um em um arquivo desta pasta:

1. `pilha_list.py`: pilha usando `list` (`append` e `pop`), incluindo o erro ao desempilhar de uma lista vazia.
2. `pilha_propria.py`: classe `Pilha` com `push`, `pop`, `peek`, `esta_vazia`, `__len__` e `__repr__`.
3. `fila_list.py`: fila usando `list` e `pop(0)`, com medição de tempo (`timeit`) para n = 10000 a 80000.
4. `fila_deque.py`: fila usando `deque` (`append` e `popleft`), comparando `list` vs `deque` e medindo o `deque` até n = 640000.
5. `fila_propria.py`: classe `Fila` sobre `deque`, com `enqueue`, `dequeue`, `primeiro`, `esta_vazia`, `__len__` e `__repr__`.
6. `balanceado.py`: verificação de parênteses, colchetes e chaves balanceados usando a `Pilha`.

## O que foi visto no módulo

- **Pilha (LIFO):** o último a entrar é o primeiro a sair (`push`, `pop`, `peek`).
- **Fila (FIFO):** o primeiro a entrar é o primeiro a sair (`enqueue`, `dequeue`).
- **`list` como pilha:** `append` e `pop` no fim da lista.
- **`list` como fila:** `pop(0)` desloca todos os elementos, custando O(n) cada vez.
- **`collections.deque`:** `append`, `appendleft`, `pop` e `popleft` em O(1); acesso por índice no meio é O(n).
- **Encapsulamento:** classes próprias que escondem a `list` ou o `deque` e expõem só as operações da pilha ou da fila.
- **`if __name__ == "__main__":`:** evita que o código de teste rode quando o arquivo é importado.
- **Aplicação:** delimitadores balanceados com pilha.

## O que foi aprendido

- Esvaziar uma fila de 80000 itens com `list.pop(0)` levou 3.4739s; com `deque.popleft()`, 0.0211s (cerca de 160x mais rápido).
- Com `list`, o tempo foi ~4x por dobra de n (O(n²) no total); com `deque`, ~2x por dobra (O(n) no total).
- `list` serve bem como pilha, mas `deque` é a escolha certa pra fila.
- Uma classe própria permite mensagens de erro próprias (`pilha vazia`, `fila vazia`) e bloqueia operações que quebram a regra da estrutura (`f[0]` dá `TypeError`).
- Na verificação de delimitadores, a **ordem** importa: `'{[(])}'` é `False` mesmo com as quantidades certas.
- Importar um arquivo executa o código solto dele; os testes devem ficar dentro do `if __name__ == "__main__":`.
- Ao ajustar o final de um arquivo, é preciso manter o resto: colar só o trecho final apagou a classe `Pilha` e causou `ImportError`.
