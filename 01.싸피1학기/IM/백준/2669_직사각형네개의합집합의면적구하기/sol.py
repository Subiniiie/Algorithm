arr = [list(map(int, input().split())) for _ in range(4)]

nemo = [[0] * 100 for _ in range(100)]

cnt = 0
for k in range(len(arr)) :
    for i in range(arr[k][0], arr[k][2]) :
        for j in range(arr[k][1], arr[k][3]) :
            if nemo[i][j] == 0 :
                nemo[i][j] = 1
                cnt += 1
print(cnt)