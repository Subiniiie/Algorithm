import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T) :
    N, M = map(int,sys.stdin.readline().split())

    up = 1
    down = 1
    temp = M - (M-N)

    i = M
    for _ in range(temp) :
        up *= i
        i -= 1
    for j in range(N, 0, -1) :
        down *= j

    print(up // down)