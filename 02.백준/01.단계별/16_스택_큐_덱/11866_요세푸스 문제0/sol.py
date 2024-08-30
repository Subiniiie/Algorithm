import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
arr = deque(i for i in range(1, N+1))
result = []

while arr :
    for i in range(K) :
        if i != K - 1 :
            a = arr.popleft()
            arr.append(a)
        else :
            a = arr.popleft()
            result.append(str(a))

print('<'+', '.join(result)+'>')