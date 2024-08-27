import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1) :
    N, M = map(int, input().split())

    arr = []
    for _ in range(N) :
        arr.append(input())
#
#     # 가로
    for i in range(N) :
        for j in range(N) :
                if j + M <= N :
                    str1 = arr[i][j:j+M]
                    str2 = str1[::-1]

                    if str1 == str2 :
                        print(f'#{tc} {str1}')

    # 세로
    total = []

    for i in range(N) :
        temp_lst = []
        for j in range(N) :
            temp_lst.append(arr[j][i])
        temp_str = ''.join(temp_lst)
        total.append(temp_str)

    for i in range(N) :
        for j in range(N) :
            if j+M <= N :
                str1 = total[i][j:j+M]
                str2 = str1[::-1]

                if str1 == str2 :
                    print(f'#{tc} {str1}')
