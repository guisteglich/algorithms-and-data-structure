"""O fatorial de um número inteiro m não negativo, é indicado por m! (lê-se "m fatorial") e é definido pela relação:

m!=m⋅(m−1)⋅(m−2)⋅(m−3)...3⋅2⋅1, para m ≥ 2.

Algumas definições são:

- 1! = 1 (fatorial de 1) - critério de parada

- 0! = 1 (fatorial de 0)
"""

def fat(m):
    if m == 1 or m == 0:
        return 1
    return m * fat(m-1)

print(fat(3))
print(fat(4))
print(fat(6))

def base_exp(a,b):
    if b == 0:
        return 1
    return a * base_exp(a, b-1)

print(base_exp(2, 0))
print(base_exp(2, 3))
print(base_exp(5, 2))