from collections import deque

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class BST:
    def __init__(self):
        self.raiz = None
        self._tamanho = 0

    def inserir(self, valor):
        novo = No(valor)
        if self.raiz is None:
            self.raiz = novo
            self._tamanho += 1
            return True
        atual = self.raiz
        while True:
            if valor == atual.valor:
                return False
            if valor < atual.valor:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    break
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo
                    break
                atual = atual.direita
        self._tamanho += 1
        return True

    def __len__(self):
        return self._tamanho

    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, resultado):
        if no is None:
            return
        self._em_ordem(no.esquerda, resultado)
        resultado.append(no.valor)
        self._em_ordem(no.direita, resultado)

    def __contains__(self, valor):
        atual = self.raiz
        while atual is not None:
            if valor == atual.valor:
                return True
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return False

    def minimo(self):
        if self.raiz is None:
            raise ValueError("arvore vazia")
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor

    def maximo(self):
        if self.raiz is None:
            raise ValueError("arvore vazia")
        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.valor
    def remover(self, valor):
        self.raiz, removido = self._remover(self.raiz, valor)
        if removido:
            self._tamanho -= 1
        return removido

    def _remover(self, no, valor):
        if no is None:
            return None, False
        if valor < no.valor:
            no.esquerda, removido = self._remover(no.esquerda, valor)
            return no, removido
        if valor > no.valor:
            no.direita, removido = self._remover(no.direita, valor)
            return no, removido
        # achou o no a remover
        if no.esquerda is None:
            return no.direita, True
        if no.direita is None:
            return no.esquerda, True
        # dois filhos: troca pelo sucessor (menor da direita)
        sucessor = no.direita
        while sucessor.esquerda is not None:
            sucessor = sucessor.esquerda
        no.valor = sucessor.valor
        no.direita, _ = self._remover(no.direita, sucessor.valor)
        return no, True

    def altura(self):
        if self.raiz is None:
            return -1
        nivel = 0
        fila = deque([self.raiz])
        while fila:
            for _ in range(len(fila)):
                no = fila.popleft()
                if no.esquerda is not None:
                    fila.append(no.esquerda)
                if no.direita is not None:
                    fila.append(no.direita)
            nivel += 1
        return nivel - 1

    @classmethod
    def de_lista_ordenada(cls, valores):
        arvore = cls()
        arvore.raiz = cls._construir(valores, 0, len(valores) - 1)
        arvore._tamanho = len(valores)
        return arvore

    @staticmethod
    def _construir(valores, inicio, fim):
        if inicio > fim:
            return None
        meio = (inicio + fim) // 2
        no = No(valores[meio])
        no.esquerda = BST._construir(valores, inicio, meio - 1)
        no.direita = BST._construir(valores, meio + 1, fim)
        return no
    def sucessor(self, valor):
        candidato = None
        atual = self.raiz
        while atual is not None:
            if valor < atual.valor:
                candidato = atual.valor
                atual = atual.esquerda
            else:
                atual = atual.direita
        return candidato

    def predecessor(self, valor):
        candidato = None
        atual = self.raiz
        while atual is not None:
            if valor > atual.valor:
                candidato = atual.valor
                atual = atual.direita
            else:
                atual = atual.esquerda
        return candidato

    def intervalo(self, a, b):
        resultado = []
        self._intervalo(self.raiz, a, b, resultado)
        return resultado

    def _intervalo(self, no, a, b, resultado):
        if no is None:
            return
        if a < no.valor:
            self._intervalo(no.esquerda, a, b, resultado)
        if a <= no.valor <= b:
            resultado.append(no.valor)
        if no.valor < b:
            self._intervalo(no.direita, a, b, resultado)


if __name__ == "__main__":
    arvore = BST()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        arvore.inserir(v)

    print("len:", len(arvore))
    print("em-ordem:", arvore.em_ordem())
    print("raiz:", arvore.raiz.valor)
    print("esq da raiz:", arvore.raiz.esquerda.valor)
    print("dir da raiz:", arvore.raiz.direita.valor)
    print("esq do 70:", arvore.raiz.direita.esquerda.valor)
    print("inserir 40 de novo:", arvore.inserir(40))
    print("len depois:", len(arvore))
    print("vazia:", BST().em_ordem())
