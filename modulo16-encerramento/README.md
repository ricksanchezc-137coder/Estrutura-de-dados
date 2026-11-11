# Módulo 16 — Encerramento: aplicar estruturas de dados ao sistema-bancario

## O que foi feito

- Revisão rápida dos Módulos 1 a 15 do Currículo 16 e uma explicação de Big-O.
- Leitura do projeto `sistema-bancario` e escolha do ponto onde uma estrutura de dados realmente ajudava: o extrato (`relatorios.py`) fazia uma consulta ao banco por transferência só pra pegar um nome.
- Passo 1 (`medir_extrato.py`): medição antes. Com n=2000 foram 2000 consultas e 1.1977s.
- Passo 2 (`medir_cache.py`): cache de nomes com `dict` e com `functools.cache`; ~15 a 17x mais rápido, saídas idênticas.
- Passo 3 (`aplicar_cache.py`): cache aplicado no `relatorios.py` (`formatar_linhas` e `buscar_nome_cacheado`). A primeira versão do script abortou sem gravar porque a assinatura real tinha anotações de tipo; a v2 aplicou 6 trocas e o `pytest` ficou igual ao de antes (171 passed, 1 failed conhecido).
- Passo 4 (`medir_depois.py`): antigo vs novo no código real, variando n e o número de destinatários distintos.

## O que foi visto no módulo

- Como aplicar estrutura de dados num projeto: achar o ponto crítico, medir antes, trocar, medir depois e conferir que o resultado é idêntico.
- Big-O mede como o tempo **cresce** com n, não os segundos; constantes não entram na classe, mas pesam na prática.
- O problema N+1 (uma consulta extra por item) e como um cache com `dict` (memoização) resolve.
- Cache de vida curta (criado por extrato) contra cache global.
- Quando a estrutura não ajuda: o SQLite já faz `ORDER BY` e `BETWEEN`, e não havia funcionalidade que pedisse heap, árvore ou grafo.

## O que foi aprendido

- Duas versões O(n) podem diferir ~16x: antigo ≈ n × (formatar + consultar), novo ≈ n × formatar + k × consultar (k = nomes distintos).
- O ganho do cache depende dos dados: ~16x com 1 destinatário, ~9x com 100, ~1.9x com 1000 e ~1x com 2000 (todos distintos), sem piora visível no pior caso.
- Ler o código real antes de editar: a cópia do repositório que consegui abrir estava desatualizada; o script que só grava quando todas as contagens batem, junto com `git diff` e `pytest`, evitou estragar o arquivo.
- Comandos novos: `git status -sb`, `grep -n -A3`, `git diff arquivo`, `PROJETO=... python script.py`.
- Mantive a compatibilidade: `formatar_transacao(t, conta_id)` continua aceitando 2 argumentos.

