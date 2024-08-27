import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수를 입력받는다
T = int(input())

# 테스트 케이스의 개수만큼 반복
for tc in range(1, T+1) :
    # N : 과목의 개수
    # K : 선택할 과목의 개수
    N, K = map(int, input().split())
    # 과목의 점수들을 담은 리스트
    arr = list(map(int, input().split()))

    # 점수들을 내림차순으로 정렬한다
    arr.sort(reverse=True)

    # K개의 과목의 점수를 더할 변수
    result = 0
    # K개를 담아야 하니까 K번만큼 반복
    for i in range(K) :
        # arr의 i번째에 있는 값을 result에 더함
        result += arr[i]

    # result의 값을 출력한다
    print(f'#{tc} {result}')