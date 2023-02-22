time = float(input("Insira o tempo gasto na viagem: "))
vel = float(input("Insira a velocidade média na viagem: "))

distancia = time * vel  

litros = distancia / 12 

print(f"O tempo gasto na viagem foi {time}")
print(f"A velocidade média da viagem foi de {vel}")
print(f"A distância percorrida na viagem foi de {distancia} Kms")
print(f"A quantidade de litros gastos na viagem foi de {litros} litros")