import sys
N = int(sys.stdin.readline())
for _ in range(N) :
    sys.stdin.readline()
    a, b, c, d = map(int, sys.stdin.readline().split())

    for i in range(d) :
        max_num = max(a, b, c)
        if max_num == a :
            a -= 1
        elif max_num == b :
            b -= 1
        else :
            c -= 1
    print(a*b*c)