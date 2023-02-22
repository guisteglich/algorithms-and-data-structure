'''Ler 5 notas e informar a média'''

# soma = 0
# for nota in range(0, 5):
#     nota = int(input("Insira a nota: "))
#     soma = soma + nota
#     print(soma)

# media = soma / 5

# print(f"A média final é {media}")

n = 1
soma = 0
while n < 6:
    nota = int(input("Insira a nota: "))
    soma = soma + nota
    n+=1

media = soma / 5

print(f"A média final é {media}")
