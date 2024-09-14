import sys
T = int(sys.stdin.readline().rstrip())


def findeCabbage(x, y) :
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for w in range(4) :
        if 0 <= x+dx[w] < M and 0 <= y+dy[w] < N :
            if arr[y+dy[w]][x+dx[w]] == 1 :
                arr[y+dy[w]][x+dx[w]] = 2
                findeCabbage(x+dx[w], y+dy[w])


for _ in range(T) :
    cnt = 0
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K) :
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    for i in range(M) :
        for j in range(N) :
            if arr[j][i] == 1 :
                cnt += 1
                arr[j][i] = 2
                findeCabbage(i, j)

    print(cnt)