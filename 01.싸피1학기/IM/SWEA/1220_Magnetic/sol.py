import sys
sys.stdin = open('input.txt')

def get_sero_cnt(col) :
    cnt = 0
    is_red = False

    for row in range(N) :
        if arr[row][col] == 1 :
            is_red = True

        elif is_red and arr[row][col] == 2 :
            cnt += 1
            is_red = False

    return cnt

for tc in range(1, 11) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_cnt = 0
    for col in range(N) :
        total_cnt += get_sero_cnt(col)

    print(f'#{tc} {total_cnt}')