import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimo_elemento = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultimo_elemento == -1:
            print("O vetor está vazio!")
        print("-----------")
        for i in range(self.ultimo_elemento + 1):
            print(i, "-----", self.valores[i])
        print("-----------")

    def insere(self, valor):
        if self.ultimo_elemento == (self.capacidade) - 1:
            print("O vetor está cheio! Não é possível adicionar o valor ", valor)
            return
        self.ultimo_elemento += 1
        self.valores[self.ultimo_elemento] = valor
    
    def pesquisa_linear(self, valor):
        for i in range(self.ultimo_elemento + 1):
            if valor == self.valores[i]:
                return i
        return -1
    
    def exclui(self, valor):
        posicao = self.pesquisa_linear(valor)
        if posicao == -1:
            return posicao
        for i in range(posicao, self.ultimo_elemento):
            self.valores[i] = self.valores[i + 1]
        self.ultimo_elemento -= 1
                      

vet1 = VetorNaoOrdenado(5)
# vet1.imprime()
vet1.insere(1)
vet1.insere(4)
vet1.insere(8)
vet1.insere(5)
vet1.insere(2)
vet1.imprime()
# print(vet1.pesquisa_linear(2))

vet1.exclui(2)
vet1.imprime()

vet1.exclui(1)
vet1.imprime()

vet1.exclui(8)
vet1.imprime()