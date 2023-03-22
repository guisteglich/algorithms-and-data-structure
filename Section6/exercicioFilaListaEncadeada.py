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
    
    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo

    def excluir_inicio(self):
        if self.__lista_vazia():
            print("A lista já está vazia! Não há o que excluir.")
            return
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo


class FilaListaEncadeada:

    def __init__(self):
        self.lista = ListaEncadeadaExtremidadeDupla()
    
    def enfileirar(self, valor):
        return self.lista.insere_final(valor)
    
    def desenfileirar(self):
        return self.lista.excluir_inicio()
    
    def fila_vazia(self):
        return self.lista.__lista_vazia()
    
    def ver_inicio(self):
        if self.lista.primeiro == None:
            return -1
        return self.lista.primeiro.valor
    

fila = FilaListaEncadeada()

fila.enfileirar(2)
fila.enfileirar(3)
print(fila.ver_inicio())
fila.desenfileirar()
print(fila.ver_inicio())