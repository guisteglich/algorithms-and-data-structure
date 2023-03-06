import numpy as np

class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade -1:
            print("A pilha está cheia")
        return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            print("A pilha está vazia!")
            return True
        else:
            return False
    
    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("A pilha está cheia! Impossível empilhar o valor ", valor)
        self.__topo +=1
        self.__valores[self.__topo] = valor

    def desempilhar(self):
        if self.__pilha_vazia():
            print("A pilha está vazia! Não há o que desempilhar.")
        self.__topo -=1
    
    def visualizar_topo(self):
        if self.__pilha_vazia():
            return -1
        return self.__valores[self.__topo]
    
pilha = Pilha(5)

# print(pilha.visualizar_topo())

pilha.empilhar(2)
print(pilha.visualizar_topo())

pilha.empilhar(3)
pilha.empilhar(5)
pilha.empilhar(7)

print(pilha.visualizar_topo())

pilha.desempilhar()
print(pilha.visualizar_topo())
pilha.desempilhar()
print(pilha.visualizar_topo())
pilha.desempilhar()
print(pilha.visualizar_topo())
pilha.desempilhar()
print(pilha.visualizar_topo())