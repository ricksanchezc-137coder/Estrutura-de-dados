# modulo6-pilhas_e_filas/balanceado.py

from pilha_propria import Pilha

pares = {")": "(", "]": "[", "}": "{"}


def balanceado(texto):
    pilha = Pilha()
    for c in texto:
        if c in "([{":
            pilha.push(c)
        elif c in pares:
            if pilha.esta_vazia() or pilha.pop() != pares[c]:
                return False
    return pilha.esta_vazia()


testes = ["()", "([]{})", "(]", "((", ")(", "", "a(b[c]d)e", "{[()]}", "{[(])}"]

for texto in testes:
    print(f"{texto!r}: {balanceado(texto)}")
