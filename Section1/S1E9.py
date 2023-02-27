'''tempo gasto na viagem e a velocidade média'''

# t = int(input("insira o tempo gasto na viagem: "))
# v = int(input("insira a velocidade média: "))

def l():
    t = int(input("insira o tempo gasto na viagem: "))
    v = int(input("insira a velocidade média: "))
    return t, v

def distancia (t, v):
    DISTANCIA = t * v
    return DISTANCIA

def qnt_l(d):
    LITROS_USADOS = d / 12
    return LITROS_USADOS

def show(d, l):
    print(f'a distancia percorrida foi {d}')
    print(f'a quantidade de litros utilizada foi de {l}')

tempo, velocidade = l()
distancia = distancia(tempo, velocidade)
quantidade_gasta = qnt_l(distancia)
show(distancia, quantidade_gasta)