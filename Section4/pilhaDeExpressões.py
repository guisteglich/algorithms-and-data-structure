import numpy as np

class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        # self.__valores = np.empty(self.__capacidade, dtype=str)
        self.__valores = np.chararray(self.__capacidade, unicode=True)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade -1:
            print("A pilha está cheia")
        return False

    def pilha_vazia(self):
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
        if self.pilha_vazia():
            print("A pilha está vazia! Não há o que desempilhar.")
        valor = self.__valores[self.__topo]
        self.__topo -=1
        return valor
    
    def visualizar_topo(self):
        if self.pilha_vazia():
            return -1
        return self.__valores[self.__topo]
    
pilha = Pilha(5)

string = input("Insira a expressão: ")

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h"]

dicionario = {"(": ")",
                "{": "}",
                "[": "]"}

for elem in string:
    if elem not in alfabeto:
        if elem in dicionario.keys():
            pilha.empilhar(elem)
        elif elem in dicionario.values():
            if pilha.pilha_vazia() or elem != dicionario[pilha.visualizar_topo()]:
                print('Erro: incorreta expressão')
                break
            else:
                if not pilha.pilha_vazia():
                    pilha.desempilhar()
        