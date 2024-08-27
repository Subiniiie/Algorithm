N, M = map(int, input().split())

arr1 = []
arr2 = []

for _ in range(N) :
    arr1.append(list(map(int, input().split())))
for _ in range(N) :
    arr2.append(list(map(int, input().split())))

arr3 = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N) :
    for j in range(M) :
        arr3[i][j] = arr1[i][j] + arr2[i][j]

    print(*arr3[i])