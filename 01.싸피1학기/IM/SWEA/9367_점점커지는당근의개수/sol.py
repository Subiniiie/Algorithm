import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    C = list(map(int, input().split()))


    cnt = 1
    max_num = 0

    for i in range(1, len(C)) :
        if C[i] == C[i-1] + 1 :
            cnt += 1
        else :
            if max_num < cnt :
                max_num = cnt
            cnt = 1
        if i == len(C)-1 :
            if max_num < cnt :
                max_num = cnt
    print(f'#{tc} {max_num}')

