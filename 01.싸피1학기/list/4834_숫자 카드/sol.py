import sys
sys.stdin = open('input.txt')

T = int(input())

# 테스트 케이스를 T개 받았으므로
# 1부터 T+1까지 반복
for test in range(1, T+1) :
    N = int(input())
    ai = list(map(int, input()))   #ai -> 0부터 9까지의 수

    # ai가 0부터 9까지의 수이므로
    # ai에 들어있는 값과 같은 수의 인덱스를 가진
    # 리스트 cnt를 만듦
    cnt = [0] * 10

    # ai를 반복하면서 얻은 card 값과
    for card in ai :
        # cnt의 인덱스인 idx값을 비교한다
        for idx in range(len(cnt)) :
            # 만약 두 값이 같으면
            # cnt의 idx 인덱스에 1을 더한다
            if card == idx :
                cnt[idx] += 1

    # cnt에서 최고값을 얻기 위해 변수 max_num을 설정한다
    # 제일 처음에는 0
    max_num = 0

    for i in range(len(cnt)) :
        # 만약 현재 cnt에 있는 값이 최고값보다 크면
        # max_num(최고값)은 현재 cnt 값인 cnt[i]가 된다
        if max_num <= cnt[i] :
            max_num = cnt[i]
            # 최고값의 인덱스를 max_idx에 저장한다
            max_idx = i
    
    # ai의 값과 인데스의 값이 같으므로
    # 최고값의 인덱스를 저장한 max_idx를 출력한다
    # max_num은 최고값이다
    print(f'#{test} {max_idx} {max_num}')