N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(101)] for _ in range(101)]

for k in range(N) :
    x, y, w, h = arr[k][0], arr[k][1], arr[k][2], arr[k][3]

    for i in range(x, x+w) :
        for j in range(y, y+h) :
            visited[i][j] = k+1



for k in range(N) :
    sum_num = 0
    for s in visited :
        for l in s :
            if l == k + 1 :
                sum_num += 1
    print(sum_num)
