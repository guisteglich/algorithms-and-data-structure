class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)
        
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                # Esquerda
                if atual.valor > valor:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        # self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        # self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return
                    
    def pesquisa(self, valor):
        atual = self.raiz
        while atual.valor != valor:
            if atual.valor > valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual == None:
                return None
        return atual
    
    def pre_ordem(self, no):
        if no != None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def ordem(self, no):
        if no != None:
            self.ordem(no.esquerda)
            print(no.valor)
            self.ordem(no.direita)

    def pos_ordem(self, no):
        if no != None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

    def excluir(self, valor):
        if self.raiz == None:
            print("A árvore está vazia")
            return
        atual = self.raiz
        pai = self.raiz
        eh_esquerda = False
        while valor != atual.valor:
            pai = atual
            if atual.valor > valor:
                eh_esquerda = True
                atual = atual.esquerda
            else:
                eh_esquerda = False
                atual = atual.direita
            
            if atual == None:
                return False
            
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None
            elif eh_esquerda:
                pai.esquerda = None
            else:
                pai.direita = None




arvore = ArvoreBinaria()

arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)


# print(arvore.raiz.direita.valor)

# print(arvore.raiz.esquerda)

# print(arvore.pesquisa(30))

# arvore.pre_ordem(arvore.raiz)

arvore.ordem(arvore.raiz)
print("--------------------")

arvore.excluir(49)

arvore.ordem(arvore.raiz)