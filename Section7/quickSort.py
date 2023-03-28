import numpy as np

def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio -1

    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i+=1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    vetor[i+1], vetor[final] = vetor[final], vetor[i+1] 
    return i + 1

def quick_sort(vetor, inicio, final):
    if inicio < final:
        posicao = particao(vetor, inicio, final)
        # Esquerda
        quick_sort(vetor, inicio, posicao - 1)
        # Direita
        quick_sort(vetor, posicao + 1, final)
    return vetor


v1=np.array([1, 4, 6, 10, 20, 2])
v2=np.array([10, 9, 8, 7, 6, 5, 4])
v3=np.array([34, 3, 8, 60])

print(quick_sort(v1, 0, len(v1) - 1))

print(quick_sort(v2, 0, len(v2) - 1))

print(quick_sort(v3, 0, len(v3) - 1))