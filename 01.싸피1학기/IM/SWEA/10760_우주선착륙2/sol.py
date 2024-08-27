import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    Aij = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    result = 0

    for i in range(N) :
        for j in range(M) :
            cnt = 0
            for k in range(8) :
                temp_i = i + dx[k]
                temp_j = j + dy[k]
                if 0 <= temp_i < N and 0 <= temp_j < M :
                    if Aij[temp_i][temp_j] < Aij[i][j] :
                        cnt += 1
            if cnt >= 4 :
                result += 1

    print(f'#{tc} {result}')