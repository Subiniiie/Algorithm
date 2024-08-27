import sys
sys.stdin = open('input.txt')

# DFS를 정의한다
# 매개변수 s는 시작점
def DFS(s) :
    # 시작점을 넣은 스택 생성
    stack = [s]
    while stack :
        # 스택은 후입선출이기에 현재 위치해 있는점은
        # 스택에서 가장 나중에 들어온 점이다
        now = stack.pop()

        # 현재 위치한 visited[now]가 0이라면 한 번도 지나가지 않았기에
        # 1을 더한다
        if visited[now] == 0 :
            visited[now] = 1

            # adj에서 now 도시가 몇 번 도시를 가는지 확인한다
            for next in range(len(adj[now])-1, 0, -1) :
                # now 도시가 갈 수 있는 next도시를 전에 지나간 적 없다면
                if visited[next] == 0 and adj[now][next] == 1 :
                    # 스택에 다음 도시를 넣기 전에
                    # next 도시가 현재 있는 도시가 갈 수 있는 도시 중에 99 도시라면
                    # 도착점이므로 1을 반환한다
                    if next == len(adj[now])-1 :
                        return 1
                    # 스택에 다음 도시를 넣는다
                    stack.append(next)
    # 99점까지 가지 못했다면 0을 반환한다
    return 0

# 테스트 케이스를 입력받는다
for _ in range(1, 11) :
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # 도시의 개수를 알기 위해 정렬한다
    sorted_arr = sorted(arr)

    # 99는 도착점이므로 99보다 작은 수 중에서 가장 큰 수를 찾는다
    for num in sorted_arr[::-1] :
        if num != 99 :
            max_num = num
            break

    # 도시의 개수 + 시작점 0 + 도착점 99를 나타내야 하기 때문에
    # 시작점~도시의 개수를 나타낸 max_num에서 2를 더해 도착점을 나타낸다
    visited = [0 for _ in range(max_num+2)]
    adj = [[0 for _ in range(max_num+2)] for _ in range(max_num+2)]

    # 화살표를 거슬러 올라갈 순 없기에 화살표가 표시하는 길만 표시한다
    for idx in range(N) :
        # 다른 도시는 인덱스와 도시 번호가 일치하지만 도차점은 무조건 99이기에
        # 만약 순서쌍에서 도착하는 곳이 99이면 인덱스의 가장 마지막에 1을 더한다
        if arr[idx*2+1] == 99 :
            adj[arr[idx*2]][-1] = 1
        else :
            adj[arr[idx*2]][arr[idx*2+1]] = 1

    # 시작점을 인자로 갖는 DFS 함수를 출력한다
    print('#{} {}'.format(tc, DFS(0)))


