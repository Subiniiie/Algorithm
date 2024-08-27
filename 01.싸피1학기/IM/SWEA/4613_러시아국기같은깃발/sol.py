import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    cnt = 0

    for first_idx in range(N-2) :
        for second_idx in range(first_idx, N-1) :
            for i in range(first_idx) :
                for j in range(M) :
                    if arr[i][j] != 'W' :
                        cnt += 1
                for k in range(second_idx) :
                    for j in range(M) :
                        if arr[k][j] != 'B' :
                            cnt += 1
                    for m in range(N-second_idx, N) :
                        for j in range(M) :
                            if arr[m][j] != 'R' :
                                cnt += 1
    print(cnt)

