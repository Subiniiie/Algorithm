# N : 가지 수, M : 두 가지가 연결된 정보의 수 V : 시작 가지
N = 4
M = 7
V = 1

# 두 가지가 연결된 걸 나타낼 2차원 배열
dfs_graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

# 반복문으로 두 가지가 연결된 걸 나타냄
for _ in range(M) :
    a, b = map(int, input().split())
    dfs_graph[a][b] = 1
    dfs_graph[b][a] = 1

# 방문했는지 확인
dfs_visited = [False for _ in range(N+1)]

# 확인할 가지들의 순서
stack = []
# 방문 순서
order = []
def dfs(start_node) :
    stack.append(start_node)

    while stack :
        v = stack.pop()
        if not dfs_visited[v]  :
            dfs_visited[v] = True
            order.append(v)

            for i in range(N, 0, -1) :
                if dfs_graph[v][i] and not dfs_visited[i] :
                    stack.append(i)
    print(*order)

from collections import deque
# N : 가지 수, M : 두 가지가 연결된 정보의 수 V : 시작 가지
N = 4
M = 7
V = 1

# 두 가지가 연결된 정보
bfs_graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    bfs_graph[a].append(b)
    bfs_graph[b].append(a)
for i in range(N+1) :
    if len(bfs_graph[i]) > 1 :
        bfs_graph[i].sort()

# 방문했는지 확인
bfs_visited = [False for _ in range(N+1)]

# 방문 순서
bfs_order = []

def bfs(start_node) :
    queue = deque([start_node])
    bfs_visited[start_node] = True
    while queue :
        v = queue.popleft()
        bfs_order.append(v)

        for i in bfs_graph[v] :
            if not bfs_visited[i] :
                queue.append(i)
                bfs_visited[i] = True
    print(*bfs_order)


