import sys
sys.stdin = open('input.txt')

# 10개의 테스트 케이스만큼 반복한다
for test in range(1, 11) :
    # 덤프횟수
    # N번 이내에서만 평탄화 해야 한다
    N = int(input())
    # 상자의 높이값들을 리스트로 표현
    arr = list(map(int, input().split()))

    # 횟수를 추가할 변수 i
    i = 0

    # i가 N보다 작을 동안 코드를 수행한다
    while i < N :
        # max() 함수로 arr의 최고값을 찾는다
        max_num = max(arr)
        # min() 함수로 arr의 최저값을 찾는다
        min_num = min(arr)
        
        # index() 함수를 이용해 arr의 최고값과 최저값의 인덱스를 찾는다
        max_idx = arr.index(max_num)
        min_idx = arr.index(min_num)

        # 최고값에서 1을 빼고, 최저값에서 1을 더한다
        arr[max_idx] -= 1
        arr[min_idx] += 1

        # 만약 최고값에서 최저값을 뺀 값이 1보다 작거나 같으면 평탄화과 완료된 것이므로
        # while문을 종료한다
        if max_num - min_num <= 1 :
            break

        # while문을 한 번 끝내면
        # i에 1을 추가한다
        i += 1

    # 덤프를 수행한 후 최고값과 최저값을 달라지므로
    # while문이 끝나면
    # 최종 최고값과 최저값을 찾는다
    max_num = max(arr)
    min_num = min(arr)

    print(f'#{test} {max_num - min_num}')


