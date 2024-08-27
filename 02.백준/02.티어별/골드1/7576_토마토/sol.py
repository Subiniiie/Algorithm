import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

arr = []
for _ in range(N) :
    arr.append(list(map(int, sys.stdin.readline().split())))

cnt = 0
temp = deque([])


def tomato() :
    while temp :
        x, y = temp.popleft()

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4) :
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if 0 <= temp_x < M and 0 <= temp_y < N and arr[temp_x][temp_y] == 0 :
                arr[temp_x][temp_y] = arr[x][y] + 1
                temp.append([temp_x, temp_y])

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 1 :
            temp.append([i, j])

tomato()

for i in arr :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt - 1)



