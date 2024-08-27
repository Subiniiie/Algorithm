import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수 입력
T = int(input())

# 테스트 케이스 개수만큼 반복
for tc in range(1, T+1) :
    # N개의 숫자열로 구성된 리스트 Ai
    # M개의 숫자열로 구성된 리스트Bj
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    # 만약 Bj가 Ai보다 길이가 길다면
    # Bj를 N개만큼 잘라야 한다
    if N < M :
        # 서로 마주보는 곱의 값을 저장할 리스트
        # 여기 있는 값들 중에서 최댓값을 찾을 거임
        result = []
        # Bj를 자를건데
        for i in range(M) :
            # 시작 숫자부터 N개 뒤에 있는 숫자가 Bj 안에 있으면
            if i + (N - 1) < M :
                # 그 숫자들을 임시 리스트 temp에 저장한다
                temp = Bj[i:i+N]
                # 마주보는 값의 곱들을 저장할 리스트
                temp_sum = []

                # temp와 Ai 둘다 N개의 숫자들을 가지고 있으니까
                # N번 반복
                for j in range(N) :
                    # 마주보는 값을 곱한 값을 temp_sum 리스트에 담는다
                    temp_sum.append(Ai[j] * temp[j])
                # 그 값들의 합을 result 리스트에 더한다
                result.append(sum(temp_sum))
    # Ai가 Bj보다 클 때도
    # 계산하는 과정은 동일
    else :
        result = []
        for i in range(N):
            if i + (M - 1) < N:
                temp = Ai[i:i + M]
                temp_sum = []

                for j in range(M):
                    temp_sum.append(Bj[j] * temp[j])
                result.append(sum(temp_sum))

    # 그렇게 구한 곱들의 값에서 가장 큰 값을 출력
    print(f'#{tc} {max(result)}')
