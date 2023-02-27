import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

sum = 0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        sum = sum + matriz[i][j]

print(sum)
