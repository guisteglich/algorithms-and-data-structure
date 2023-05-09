def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]

        return quickSort(menores) + [pivo] + quickSort(maiores)
    
arr = [30, 5, 2, 9, 145, 9]

print(quickSort(arr))