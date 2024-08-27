import sys
A, B = map(int, sys.stdin.readline().split())
aa, bb = A, B
A, B = min(A, B), max(A, B)

while A != 0 :
    B = B % A
    A, B = B, A
print(aa * bb // B)