import sys
sys.stdin = open('input.txt')

for tc in range(1, 11) :
    N = int(input())
    L = 8

    result = []

    arr = []
    for _ in range(L) :
        arr.append(input())

    # 가로
    for i in range(L) :
        for j in range(L) :
            if j + N <= L :
                if arr[i][j:j+N] == arr[i][j:j+N][::-1] :
                    result.append(arr[i][j:j+N])

    # 세로
    for i in range(L) :
        temp_lst = []
        for j in range(L) :
            if j + N <= L :
                print(arr[j:j+N][i])