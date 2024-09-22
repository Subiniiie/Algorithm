from collections import deque
import sys


def bfs() :
    q = deque()
    q.append(N)

    while q :
        x = q.popleft()

        if x == K :
            print(arr[x])
            break
        else :
            for i in (x-1, x+1, x*2) :
                if 0 <= i < limit and not arr[i] :
                    arr[i] = arr[x] + 1
                    q.append(i)

N, K = map(int, sys.stdin.readline().split())
limit = 100000 + 1
arr = [0 for _ in range(limit)]

bfs()