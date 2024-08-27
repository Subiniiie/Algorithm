import sys
sys.stdin = open('input.txt')

# 테스트 케이스의 개수를 입력받는다
T = int(input())

# 테스트 케이스의 개수만큼 반복한다
for tc in range(1, T+1) :
    # N : 수강생 총 인원
    # K : 과제를 제출한 사람의 수
    N, K = map(int, input().split())
    # 과제를 제출한 사람의 번호
    number = list(map(int, input().split()))

    # 과제를 제출 안 한 사람의 번호를 담을 리스트
    result = []
    # 번호가 1부터 N까지니까 반복문의 범위는 (1, N+1)
    for i in range(1, N+1) :
        # 순서대로 번호를 살펴보는데 만약 그 번호가 number에 없으면
        # 제출을 안 한 거니까
        if i not in number :
            # result에 그 번호를 추가한다
            result.append(i)

    # result의 값만 출력
    print(f'#{tc}', *result)