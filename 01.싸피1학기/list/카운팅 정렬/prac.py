def CountingSort(data, temp, k) :

    counts = [0] * (k+1)

    for i in range(len(data)) :
        counts[data[i]] += 1

    for j in range(1, len(counts)) :
        counts[j] = counts[j-1] + counts[j]

    for i in range(len(data)-1, -1, -1) :
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]
    return temp

print(CountingSort([0, 1, 2, 1, 2, 3, 1], [0, 0, 0, 0, 0, 0, 0], 3))
