import numpy as np

def merge_sort(vetor):
    if len(vetor) > 1:
        divisao = int(len(vetor) // 2)
        esquerda = vetor[:divisao].copy()
        direita = vetor[divisao:].copy()

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        #Ordenar a esquerda e direita
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i+=1
            else:
                vetor[k] = direita[j]
                j+=1
            k+=1
        
        # Ordenação final
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            vetor[k] = direita[j]
            j += 1
            k += 1
    return vetor

print(merge_sort(np.array([1, 4, 6, 10, 20, 2])))

print(merge_sort(np.array([10, 9, 8, 7, 6, 5, 4])))

print(merge_sort(np.array([34, 3, 8, 60])))