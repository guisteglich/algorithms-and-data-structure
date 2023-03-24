import numpy as np

def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(n - i - 1):
            if vetor[j] > vetor[j+1]:
                temp = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = temp

    return vetor

print(bubble_sort(np.array([1, 4, 6, 10, 20, 2])))

print(bubble_sort(np.array([10, 9, 8, 7, 6, 5, 4])))