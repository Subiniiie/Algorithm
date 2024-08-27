import sys
sys.stdin = open('input.txt')

# 테스트 케이스 T개를 입력받는다
T = int(input())

# T개 만큼 반복하며 테스트 케이스의 답을 출력한다
for test in range(1, T+1) :
    # N : 칠해야 할 영역의 개수
    N = int(input())
    # 10:10 격자 내부에서 일어나는 일이니까
    # 행이 10이고 열이 10인 영역을 만든다
    arr = [[0 for _ in range(10)] for _ in range(10)]
    
    # N개를 칠해야 하니까 N번 반복
    for i in range(N) :
        # r1와 c1은 상자의 왼쪽 모서리의 행과 열 값이다
        # r2와 c2는 상자의 오른쪽 모서리의 행과 열 값이다
        # [r1, c1] ~ [r2, c2] 영역에 상자가 있다
        r1, c1, r2, c2, color = map(int, input().split())
        
        # 상자의 가장 왼쪽 행부터 가장 오른쪽 행까지 반복한다
        for r in range(r1, r2+1) :
            # 상자의 가장 왼쪽 열부터 가장 오른쪽 열까지 반복한다
            for c in range(c1, c2+1) :
                # arr[r][c]가 0이면 아무것도 칠해져 있지 않은 칸
                # arr[r][c]가 1이면 빨간색이 칠해져 있는 칸
                # arr[r][c]가 2면 파란색이 칠해져 있는 칸
                # 보라색이 칠해져 있는 칸은 빨간색+파란색이므로 3이다
                # 만약 상자에 있는 어떤 칸이 0일 때
                if arr[r][c] == 0 :
                    # color가 1이면
                    if color == 1 :
                        #그 칸은 1이다
                        arr[r][c] = 1
                    # color가 2면
                    elif color == 2 :
                        # 그 칸은 2다
                        arr[r][c] = 2
                # 만약 상자에 있는 어떤 칸이 1일 때
                # 빨간색이 칠해져 있는 칸
                elif arr[r][c] == 1 :
                    # color가 2이면 파란색을 칠해야 하는데
                    # 빨간색이 이미 칠해져 있으므로
                    if color == 2 :
                        # 그 칸은 3(보라색)이 된다
                        arr[r][c] = 3
                # 만약 상자에 있는 어떤 칸이 2일 때
                elif arr[r][c] == 2 :
                    # color가 1이면 빨간색이 칠해야 하는데
                    # 파란색이 이미 칠해져 있으므로
                    if color == 1 :
                        # 그 칸은 3(보라색)이 된다
                        arr[r][c] = 3

    # arr[r][c]가 3인 모든 값의 개수를 구한다
    # 개수를 셀 거니까 제일 처음은 0
    cnt = 0
    # arr 안에 리스트가 있으므로
    # arr의 길이만큼 반복한다
    for j in range(len(arr)) :
        # arr[j]에서 3의 개수를 구하고
        # cnt에 더한다
        cnt += arr[j].count(3)

    print(f'#{test} {cnt}')








