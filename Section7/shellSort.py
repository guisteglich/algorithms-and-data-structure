import numpy as np

def shell_sort(vetor):
    intervalo = int(len(vetor) / 2)

    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            vetor[j] = temp
        intervalo //= 2

    return vetor

print(shell_sort(np.array([1, 4, 6, 10, 20, 2])))

print(shell_sort(np.array([10, 9, 8, 7, 6, 5, 4])))

print(shell_sort(np.array([34, 3, 8, 60])))