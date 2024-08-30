import sys
from collections import deque

d = deque()
N = int(sys.stdin.readline().rstrip())

for _ in range(N) :
    temp = list(sys.stdin.readline().split())
    if int(temp[0]) == 1 :
        d.appendleft(int(temp[1]))
    elif int(temp[0]) == 2 :
        d.append(int(temp[1]))
    elif int(temp[0]) == 3 :
        if d :
            print(d.popleft())
        else :
            print(-1)
    elif int(temp[0]) == 4 :
        if d :
            print(d.pop())
        else :
            print(-1)
    elif int(temp[0]) == 5 :
        print(len(d))
    elif int(temp[0]) == 6 :
        if d :
            print(0)
        else :
            print(1)
    elif int(temp[0]) == 7 :
        if d :
            print(d[0])
        else :
            print(-1)
    else :
        if d :
            print(d[-1])
        else :
            print(-1)

