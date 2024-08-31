import sys
N, K = map(int, sys.stdin.readline().split())

up = 1
down = 1
temp = N - (N - K)
i = N
for _ in range(temp) :
    up *= i
    i -= 1
for j in range(1, K+1) :
    down *= j

print(up // down)