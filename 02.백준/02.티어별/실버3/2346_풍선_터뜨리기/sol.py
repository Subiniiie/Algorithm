import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

q = deque(enumerate(map(int, input().split())))
result = []

while q :
    idx, paper = q.popleft()
    result.append(idx + 1)

    if paper > 0 :
        q.rotate(-(paper - 1))
    elif paper < 0 :
        q.rotate(-paper)

print(' '.join(map(str, result)))


