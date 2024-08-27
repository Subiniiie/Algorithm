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
    # 보라색의 개수를 구해야 하기 때문에
    # 제일 처음에는 0으로 설정한다
    purple = 0

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
                # 만약 arr[r][c]가 0이라면
                # 아무것도 칠해지지 않았다는 뜻이므로
                if arr[r][c] == 0 :
                    # color 값으로 설정한다
                    arr[r][c] = color
                # arr[r][c]가 0이 아니라면
                # 이미 다른 색이 색칠 되어있다는 뜻이므로
                # 그 칸은 또 다른 색이 칠해져 보라색이 된다
                else :
                    # 보라색을 구하는 변수에 1을 더한다
                    purple += 1

    print(f'#{test} {purple}')