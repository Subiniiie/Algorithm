n = int(input())
arr = list(map(int, input().split()))

line = [0 for _ in range(n+1)]

for i in range(len(arr)) :
    if i == 0 :
        line[1] = 1
    else :
        if line[arr[i]+1] == 0 :
            line[arr[i]+1] = i + 1
        elif line[arr[i]+1] != 0 :
            for j in range(len(line)-1, arr[i], -1) :
                if line[j] != 0 :
                    line[j], line[j+1] = line[j+1], line[j]
            line[arr[i] + 1] = i + 1


line.reverse()
print(*line[:-1])

