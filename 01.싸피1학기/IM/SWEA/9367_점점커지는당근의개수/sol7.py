import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    C = list(map(int, input().split()))

    cnt = 1
    result = []

    for i in range(N) :
        if i == N-1 :
            result.append(cnt)
        elif C[i] < C[i+1] :
            cnt += 1
        else :
            result.append(cnt)
            cnt = 1
    print(f'#{tc} {max(result)}')