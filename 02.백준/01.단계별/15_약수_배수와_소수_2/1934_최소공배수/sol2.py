import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T) :
    A, B = map(int, sys.stdin.readline().split())

    aa, bb = A, B
    while A != 0 :
        A, B = min(A, B), max(A, B)
        B = B % A
        A, B = B, A

    print(aa * bb // B)