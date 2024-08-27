import sys
sys.stdin = open('input.txt')

# 테스트 케이스를 입력받음
T = int(input())

# 테스트 케이스의 개수만큼 반복한다
for tc in range(1, T+1) :
    # N : 농장의 크기 / 홀수임
    N = int(input())
    # 농작물을 가치를 입력받음
    farm = [list(map(int, input())) for _ in range(N)]

    # 농장의 가운데 줄은 모든 농장물을 수확할 수 있음
    # 가운데 줄의 인덱스를 구함
    k = N // 2

    # 농작물의 가치를 담을 리스트 생성
    result = []

    # 가운데 줄의 모든 농작물의 가치를 result에 더해주기 위해 N만큼 반복
    for i in range(N) :
        result.append(farm[k][i])

    # 가운데 줄을 기준으로 위와 아래는 같은 범위에 있는 농작물을 수확해야 함
    # 위쪽은 k-1번부터 0번 인덱스까지
    # 아래쪽은 k+1번부터 N-1번 인덱스까지
    for j in range(1, k+1) :
        # a는 위쪽 지역, 한 행씩 줄어들고 왼쪽과 오른쪽에 있는 칸이 한 칸씩 줄어든다
        # b는 아래쪽 지역, 한 행씩 많아지고 왼쪽과 오른쪽에 있는 칸이 한 칸씩 줄어든다
        a = farm[k-j][j:N-j]
        b = farm[k+j][j:N-j]

        # a와 b 리스트에 담겨져 있는 값을 
        # 반복문을 통해 result에 담아준다
        for l in range(len(a)) :
            result.append(a[l])
            result.append(b[l])

    # result에 담긴 모든 값을 sum 함수를 통해 더한다
    print(f'#{tc} {sum(result)}')