class No:
    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostra_no(self):
        return self.valor

class ListaEncadeada:
    
    def __init__(self):
        self.primeiro =  None

    def insere_primeiro(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def excluir_inicio(self):
        if self.primeiro == None:
            print("A lista está vazia!")
            return None
        
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp


class PilhaListaEncadeada:

    def __init__(self):
        self.lista = ListaEncadeada()

    def empilhar(self, valor):
        return self.lista.insere_primeiro(valor)

    def desempilhar(self):
        return self.lista.excluir_inicio()
    
    def pilha_vazia(self):
        self.lista.primeiro == None

    def ver_topo(self):
        if self.lista.primeiro == None:
            return -1
        return self.lista.primeiro.valor


    # def empilhar(self, valor):
    #     novo = No(valor)
    #     if self.primeiro.proximo == None:
    #         self.primeiro = novo
    #     atual = self.primeiro
    #     while atual.proximo != None:
    #         atual = atual.proximo
    #     atual.proximo = novo

    #     return novo
    
    # def desempilhar(self):
    #     if self.pilha_vazia():
    #         print("A pilha está vazia! Não há o que desempilhar.")
    #         return
    #     atual = self.primeiro
    #     while atual.proximo != None:
    #         atual = atual.proximo
    #     if atual.proximo == None:
    #         self.primeiro = None        
    #     return atual
    
    # def pilha_vazia(self):
    #     return self.primeiro == None

    # def ver_topo(self):
    #     if self.pilha_vazia():
    #         print("A pilha está vazia!")
    #         return
    #     atual = self.primeiro
    #     while atual.proximo != None:
    #         atual = atual.proximo
    #     print(atual.mostra_no())


pilha = PilhaListaEncadeada()

pilha.empilhar(20)
pilha.empilhar(40)

print(pilha.ver_topo())

pilha.empilhar(60)
pilha.empilhar(80)
print(pilha.ver_topo())

pilha.desempilhar()
print(pilha.ver_topo())