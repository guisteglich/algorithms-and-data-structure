
import numpy as np

class VetorOrdenado:
  
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        print("-----------")
        for i in range(self.ultima_posicao + 1):
            print(i, ' - ', self.valores[i])
        print("-----------")

    # O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor or i == self.ultima_posicao:
                return -1
            if self.valores[i] == valor:
                return i 
    
    def pesquisa_binaria(self, valor):
        limite_superior = self.ultima_posicao
        limite_inferior = 0

        while True:
            posicao_atual = int((limite_superior + limite_inferior)/2)
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif limite_inferior > limite_superior:
                return -1
            else:                
                if self.valores[posicao_atual] > valor:
                    limite_superior = posicao_atual - 1
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1

        
            
    def exclui(self, valor):
        posicao = self.pesquisa(valor)
        print("essa é a posição: ", posicao)
        if posicao == -1:
            return posicao
        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i + 1]
        self.ultima_posicao -= 1



vetor = VetorOrdenado(10)
vetor.imprime()

vetor.insere(6)
# vetor.imprime()

vetor.insere(4)
# vetor.imprime()

vetor.insere(3)
# vetor.imprime()

vetor.insere(5)
# vetor.imprime()

vetor.insere(1)
# vetor.imprime()

vetor.insere(8)
vetor.exclui(8)
vetor.imprime()

# print(vetor.pesquisa(4))

print(vetor.pesquisa_binaria(1))
print(vetor.pesquisa_binaria(4))
print(vetor.pesquisa_binaria(8))

# vetor.exclui(4)
# vetor.imprime()
