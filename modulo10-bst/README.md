# Módulo 10 — Árvores binárias de busca (BST)

Currículo 16 (Estruturas de dados). Módulo isolado do sistema-bancario.

## O que foi feito

Todo o código está na classe `BST` (e na classe `No`) em `bst_basico.py`; cada passo tem um arquivo de teste.

| Passo | Arquivo | O que foi feito |
|---|---|---|
| 1 | `bst_basico.py` | `No`, `BST`, `inserir` (ignora repetidos), `__len__`, `em_ordem` |
| 2 | `busca.py` | `__contains__`, `minimo`, `maximo` |
| 3 | `remover.py` | `remover` com os 3 casos (folha, um filho, dois filhos via sucessor) |
| 4 | `custo_altura.py` | `altura` iterativa; inserção ordenada vs aleatória (altura e tempo) |
| 5 | `equilibrada.py` | `de_lista_ordenada` (elemento do meio como raiz); busca na degenerada vs equilibrada |
| 6 | `validar.py` | validação ingênua vs com limites; árvore "armadilha" |
| 7 | `intervalo.py` | `sucessor`, `predecessor`, `intervalo` com poda |

Como rodar (dentro da pasta do módulo): `python <arquivo>.py`

Resultados principais:

- Valores ordenados: altura = n − 1 (n=4000 → 3999); valores aleatórios: altura 26 com n=4000.
- Com n=4000, inserir ordenado levou 1.4994s contra 0.0154s no aleatório (~97x).
- Equilibrada: altura = floor(log₂ n) (n=1000 → 9, n=4000 → 11, n=100000 → 16); com n=4000 as buscas foram ~236x mais rápidas que na degenerada.
- Validação: a árvore "armadilha" enganou a checagem ingênua (True) e foi pega pela versão com limites (False).
- Intervalo com poda em n=100000: 11.6 µs contra 51.58 ms de `em_ordem` + filtro (~4449x).

## O que foi visto no módulo

- Regra da BST: esquerda menor, direita maior, em **toda** a subárvore.
- Buscar, inserir e remover custam O(h); h é ~log₂ n se equilibrada e n − 1 se degenerada.
- A em-ordem de uma BST válida sai ordenada.
- Remoção com dois filhos: trocar pelo sucessor (menor da subárvore direita).
- A ordem de inserção define a forma da árvore; dados ordenados geram uma árvore degenerada.
- Construir a partir de lista ordenada, pegando o meio como raiz, dá árvore equilibrada.
- Árvores que se autoequilibram (AVL, rubro-negra) existem para evitar o pior caso.
- Sucessor/predecessor por descida única; intervalo por em-ordem com poda, O(h + k).
- Validar uma BST exige limites herdados dos ancestrais, não só a comparação com os filhos.

## O que foi aprendido

- O custo de uma BST vem da **altura**, não do número de nós: os mesmos dados deram 0.0154s ou 1.4994s dependendo da ordem.
- Conferir só os filhos diretos engana: o 6 sob o 15, à direita do 10, passou na checagem ingênua.
- A poda faz o intervalo evitar percorrer a árvore toda (11.6 µs contra 51.58 ms).
- Escrever a altura de forma iterativa evita depender do limite de recursão (Módulos 8 e 9).
- Remover com um desenho no papel antes de rodar ajudou a prever a nova raiz (65, o sucessor do 50).

