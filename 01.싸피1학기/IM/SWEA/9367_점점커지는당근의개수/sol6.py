import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))

    i = 1
    cnt = 1
    max_num = 0
    while i < N :
        if C[i] == C[i-1] + 1 :
            cnt += 1
        else :
            temp_max = C[i-1]
            if max_num < temp_max :
                max_num = temp_max
        i += 1
    print(cnt)