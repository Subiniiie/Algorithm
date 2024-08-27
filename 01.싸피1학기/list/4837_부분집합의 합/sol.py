import sys
sys.stdin = open('input.txt')

# 1부터 12까지 있는 집합 A
A = [_ for _ in range(1, 13)]

# 테스트 케이스 수를 입력받는다
T = int(input())

# 테스트 케이스의 수만큼 반복
for test in range(1, T+1) :
    # N은 부분집합에서 원소의 개수이고
    # K는 부분집합의 합이다
    N, K = map(int, input().split())

    # 조건을 만족하는 부분집합으 개수를 변수 cnt로 지정
    # 제일 처음은 0개
    cnt = 0

    # 부분집합은 A의 모든 원소가 있는지 없는지 알아야 해서
    # 2의 12제곱만큼 반복한다
    for i in range(1 << len(A)) :
        # 임시로 부분집합을 넣을 리스트 lst를 만든다
        # 이 리스트의 원소의 개수와 원소의 합을 알거임
        lst = []
        # A의 길이만큼 반복한다
        for j in range(len(A)) :
            # 만약 i의 2진수값과 12개의 0 중 j번째에 1이 있는 값이 일치하면
            if i & (1 << j) :
                # lst에 A[j]의 값을 추가한다
                lst.append(A[j])
        # 만약 lst의 길이가 N과 일치하고
        # lst에 있는 숫자들의 합이 K와 일치하면
        if len(lst) == N and sum(lst) == K :
            # 조건을 만족하는 부분집합은 1개 더 늘어난다
            cnt += 1

    print(f'#{test} {cnt}')