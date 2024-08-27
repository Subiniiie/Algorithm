import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    str1 = input()
    str2 = input()

    cnt_lst = []
    for i in str1 :
        cnt = 0
        for j in str2 :
            if i == j :
                cnt += 1
        cnt_lst.append(cnt)
    print(f'#{tc} {max(cnt_lst)}')