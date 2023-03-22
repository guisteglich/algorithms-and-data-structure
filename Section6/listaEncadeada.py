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

    def mostrar(self):
        if self.primeiro == None:
            print("A lista está vazia!")
            return None
        
        atual = self.primeiro
        while atual != None:
            print(atual.mostra_no())
            atual = atual.proximo

    def pesquisa(self, valor):
        if self.primeiro == None:
            print("A lista está vazia!")
            return None
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                print(f"O {valor} não está na lista!")
                return None
            else:
                atual = atual.proximo
        return atual

    def excluir_inicio(self):
        if self.primeiro == None:
            print("A lista está vazia!")
            return None
        
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp
    
    def excluir_valor(self, valor):
        if self.primeiro == None:
            print("A lista está vazia!")
            return None
        anterior = self.primeiro
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo == None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo

        return atual




    
# no1 = No(1)
# print(no1.mostra_no())

lista = ListaEncadeada()
lista.insere_primeiro(1)

lista.insere_primeiro(3)
lista.insere_primeiro(6)
lista.mostrar()
print("--------------")
lista.excluir_inicio()
lista.mostrar()
# print("--------------")
# lista.excluir_inicio()
# lista.mostrar()
# print("--------------")
# lista.excluir_inicio()
# lista.mostrar()

print(lista.pesquisa(6))

lista.insere_primeiro(1)
lista.insere_primeiro(8)
lista.insere_primeiro(6)
lista.mostrar()
print("--------------")

lista.excluir_valor(8)
print("--------------")
lista.mostrar()
lista.excluir_valor(6)
print("--------------")
lista.mostrar()
lista.excluir_valor(3)
print("--------------")
lista.mostrar()
lista.excluir_valor(1)
print("--------------")
lista.mostrar()