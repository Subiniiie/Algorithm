
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    max_num = 0
    for i in range(N) :
        for j in range(M) :
           temp = arr[i][j]
           for k in range(4) :
               for s in range(1, arr[i][j]+1) :
                   temp_x = i + dx[k] * s
                   temp_y = j + dy[k] * s
                   if 0 <= temp_x < N and 0 <= temp_y < M :
                       temp += arr[temp_x][temp_y]
           if max_num < temp :
               max_num = temp
    print(f'#{tc} {max_num}')

