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
        
        # Busca pelo valor que será excluído
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

        # O nó a ser apagado é um nó folha 
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None
            elif eh_esquerda:
                pai.esquerda = None
            else:
                pai.direita = None

        # O nó a ser apagado possui só um filho a esquerda
        elif atual.direita == None:
            if atual == self.raiz:
                self.raiz = atual.esquerda
            elif eh_esquerda:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda

        # O nó a ser apagado possui só um filho a direita
        elif atual.esquerda == None:
            if atual == self.raiz:
                self.raiz = atual.direita
            elif eh_esquerda:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita

        # O nó possui dois filhos
        else:
            sucessor = self.sucessor(atual)

            if self.raiz == atual:
                self.raiz = sucessor
            elif eh_esquerda:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor

        return True

    def sucessor(self, no):
        sucessor = no
        pai_sucessor = no
        atual = no.direita

        while atual != None:
            pai_sucessor = sucessor
            sucessor = atual 
            atual = atual.esquerda

        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
        
        return sucessor


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

arvore.excluir(14)

arvore.ordem(arvore.raiz)
print("--------------------")

arvore.excluir(39)

arvore.ordem(arvore.raiz)
print("--------------------")

# arvore.excluir(34)

arvore.excluir(30)

arvore.ordem(arvore.raiz)
print("--------------------")