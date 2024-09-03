import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
arr = [list(map(str, sys.stdin.readline().split())) for _ in range(1, 1+N)]

dance_status = {}
dance_status['ChongChong'] = True
queue = deque(['ChongChong'])

while queue :
    current = queue.popleft()
    for a, b in arr :
        if current in (a, b) :
            other = a if current == b else b
            if other not in dance_status :
                dance_status[other] = True
                queue.append(other)
print(len(dance_status))