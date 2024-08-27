N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

visited = [[0 for _ in range(1001)] for _ in range(1001)]

for k in range(N) :
    i = arr[k][0]
    j = arr[k][1]

    for w in range(arr[k][2]) :
        for s in range(arr[k][3]) :
            visited[i+w][j+s] = k+1


for l in range(N) :


