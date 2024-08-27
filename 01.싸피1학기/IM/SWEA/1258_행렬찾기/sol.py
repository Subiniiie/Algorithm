import sys
sys.stdin = open('input.txt')

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
route = []

def DFS(x, y) :
    if visited[x][y] == 0 :
        visited[x][y] = 1

        route.append([x, y])


        for i in range(4) :
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if 0 <= temp_x < n and 0 <= temp_y < n :
                if visited[temp_x][temp_y] == 0 and arr[temp_x][temp_y] != 0 :

                    DFS(temp_x, temp_y)
    return route


T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
    route = []

    for k in range(n) :
        for l in range(n) :
            if visited[k][l] == 0 and arr[k][l] != 0 :
                result = DFS(k, l)
    print(f'# {tc} {result}')