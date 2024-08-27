import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))

    cnt = 1
    result = []

    for i in range(1, len(C)):
        if C[i] == C[i - 1] + 1:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 1
        if i == len(C) - 1:
            result.append(cnt)
    print(f'#{tc} {max(result)}')