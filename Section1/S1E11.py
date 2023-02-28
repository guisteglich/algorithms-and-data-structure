''''Crie uma classe chamada aluno com os seguintes atributos:
- Nome
- Nota 1
- Nota 2
- Crie um construtor para a classe (__init__)

Crie as seguintes funções (métodos):
- Calcula média, retornando a média aritmética entre as notas
- Mostra dados, que somente imprime o valor de todos os atributos
- Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)

'''

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome 
        self.nota1 = nota1
        self.nota2 = nota2

    def mean(self):
        return (self.nota1 + self.nota2)/2
    
    def show(self):
        print(f'O nome do aluno é: {self.nome}')
        print(f'Sua primeira nota foi: {self.nota1}')
        print(f'Sua segunda nota foi: {self.nota2}')

    def approved(self, mean):
        if mean >= 6:
            return f'{self.nome} está aprovado pois ficou com {mean} de média'        
        return f'{self.nome} está reprovado com média {mean}'


aluno1 = Aluno("Guilherme", 10, 9)
aluno2 = Aluno("Pedro", 5, 6)

aluno1.show()
media = aluno1.mean()
isApproved = aluno1.approved(media)
print(isApproved)


aluno2.show()
media = aluno2.mean()
isApproved = aluno2.approved(media)
print(isApproved)

# print(media)
# aluno2.show()