def SelectionSort(arr, N) :

    for i in range(N-1) :
        min_idx = i
        for j in range(i+1, N) :
            if arr[i] > arr[j] :
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


print(SelectionSort([1, 4, 3, 2, 6, 0], 6))
