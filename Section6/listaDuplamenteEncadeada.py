class No:
    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostra_no(self):
        return self.valor

class ListaDuplamenteEncadeada:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __lista_vazia(self):
        return self.primeiro == None
    
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo

    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print("A lista está vazia!")
            return
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None
        self.primeiro = self.primeiro.proximo
        return temp
    
    def excluir_final(self):
        if self.__lista_vazia():
            print("A lista está vazia!")
            return
        temp = self.ultimo
        if self.primeiro.proximo == None:
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None
        self.ultimo = self.ultimo.anterior
        return temp

    def mostra_frente(self):
        atual = self.primeiro
        while atual != None:
            print(atual.mostra_no())
            atual = atual.proximo
    
    def mostra_tras(self):
        atual = self.ultimo
        while atual != None:
            print(atual.mostra_no())
            atual = atual.anterior

lista = ListaDuplamenteEncadeada()

lista.insere_inicio(1)
lista.insere_inicio(2)
print("Frente")
lista.mostra_frente()
print("Trás")
lista.mostra_tras()
print("----------")
lista.insere_final(3)
lista.insere_final(4)
print("Frente")
lista.mostra_frente()
lista.excluir_final()
print("trás")
lista.mostra_tras()
