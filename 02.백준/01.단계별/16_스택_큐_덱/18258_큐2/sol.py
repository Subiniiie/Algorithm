import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

queue = deque()
for _ in range(N) :
    temp = list(sys.stdin.readline().split())
    if temp[0] == 'push' :
        queue.append(int(temp[1]))
    elif temp[0] == 'pop' :
        if queue :
            print(queue.popleft())
        else :
            print(-1)
    elif temp[0] == 'size' :
        print(len(queue))
    elif temp[0] == 'empty' :
        if queue :
            print(0)
        else :
            print(1)
    elif temp[0] == 'front' :
        if queue :
            print(queue[0])
        else :
            print(-1)
    else :
        if queue :
            print(queue[-1])
        else :
            print(-1)