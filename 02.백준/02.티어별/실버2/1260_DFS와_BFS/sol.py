import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
dfs_graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
bfs_graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    dfs_graph[a][b] = 1
    dfs_graph[b][a] = 1
    bfs_graph[a].append(b)
    bfs_graph[b].append(a)
for i in range(N+1) :
    if len(bfs_graph[i]) > 1 :
        bfs_graph[i].sort()
    bfs_graph[i].sort()
dfs_visited = [False for _ in range(N+1)]
stack = []
dfs_order = []
def dfs(start_node) :
    stack.append(start_node)

    while stack :
        v = stack.pop()
        if not dfs_visited[v] :
            dfs_visited[v] = True
            dfs_order.append(v)

            for i in range(N, 0, -1) :
                if dfs_graph[v][i] and not dfs_visited[i] :
                    stack.append(i)
    print(*dfs_order)

bfs_visited = [False for _ in range(N+1)]
bfs_order = []
def bfs(bfs_graph, start, bfs_visited) :
    queue = deque([start])
    bfs_visited[start] = True
    while queue :
        v = queue.popleft()
        bfs_order.append(v)

        for i in bfs_graph[v] :
            if not bfs_visited[i] :
                queue.append(i)
                bfs_visited[i] = True
    print(*bfs_order)


dfs(V)
bfs(bfs_graph, V, bfs_visited)


