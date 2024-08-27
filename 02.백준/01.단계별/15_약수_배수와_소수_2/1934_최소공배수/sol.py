import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    i = 1
    while True :
        if (b * i) % a == 0 :
            print(b * i)
            break
        else :
            i += 1
