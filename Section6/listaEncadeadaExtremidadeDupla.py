import numpy as np

class No:
    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        return self.valor
    
class ListaEncadeadaExtremidadeDupla:
    
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None
    
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo
    
    def mostrar(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return
        atual = self.primeiro
        while atual != None:
            print(atual.mostra_no())
            atual = atual.proximo   

    def excluir_inicio(self):
        if self.__lista_vazia():
            print("A lista já está vazia! Não há o que excluir.")
            return
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo


lista = ListaEncadeadaExtremidadeDupla()

lista.insere_inicio(1)
#print(lista.primeiro, lista.ultimo)

lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)

lista.mostrar()
print("---------")
lista.insere_final(8)
lista.mostrar()

lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()
lista.excluir_inicio()


