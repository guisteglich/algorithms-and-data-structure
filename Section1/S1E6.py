d = {}

for i in range(0, 3):
    n = input("Insira o nome: ")
    v = int(input("Insira a nota: "))
    d[n] = v

print(d)

sum = 0
for elem in d.values():
    sum = sum + elem

m = sum / len(d)

print(m)