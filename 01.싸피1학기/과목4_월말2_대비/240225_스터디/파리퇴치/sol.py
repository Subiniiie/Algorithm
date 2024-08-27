import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = []
    for i in range(N) :
        for j in range(N) :
            temp = 0
            for w in range(M) :
                for k in range(M) :
                    temp_i = i + w
                    temp_j = j + k
                    if 0 <= temp_i < N and 0 <= temp_j < N :
                        temp += arr[temp_i][temp_j]
            result.append(temp)

    print(f'#{tc} {max(result)}')


