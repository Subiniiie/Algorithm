import sys
N, M = map(int, sys.stdin.readline().strip().split())
s = []
visited = [False] * (N+1)

def dfs() :
    if len(s) == M :
        print(' '.join(map(str, s)))
        return
    for i in range(1, N+1) :
        if visited[i] :
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False

dfs()