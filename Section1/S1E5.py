l = []
for i in range(0, 5):
    n = int(input("Insira o número inteiro: "))
    l.append(n)

sum = 0
for elem in l:
    sum = sum + elem

print(sum)