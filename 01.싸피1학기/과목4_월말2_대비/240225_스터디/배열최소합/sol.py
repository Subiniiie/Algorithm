import sys
sys.stdin = open('input.txt')

def f(i, s, N) :
    global min_num

    if i == N :
        if min_num > s :
            min_num = s

    elif min_num < s :
        return

    else :
        for j in range(i, N) :
            p[i], p[j] = p[j], p[i]
            f(i+1, s+arr[i][p[i]], N)
            p[i], p[j] = p[j], p[i]

    return min_num


T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    min_num = 100

    print(f'#{tc} {f(0, 0, N)}')