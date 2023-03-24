import numpy as np

def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        id_min = i
        for j in range(i+1, n):
            if vetor[id_min] > vetor[j]:
                id_min = j
        temp = vetor[i]
        vetor[i] = vetor[id_min]
        vetor[id_min] = temp
    return vetor

print(selection_sort(np.array([1, 4, 6, 10, 20, 2])))

print(selection_sort(np.array([10, 9, 8, 7, 6, 5, 4])))