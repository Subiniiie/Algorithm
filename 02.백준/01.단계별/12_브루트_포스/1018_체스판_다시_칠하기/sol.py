# N 세로, M 가로
N, M = map(int, input().split())
arr = [[i for i in input()] for _ in range(N)]

result = 50 * 50 + 1

for i in range(0, N-7) :
    for j in range(0, M-7):
        b_s = 0
        w_s = 0
        for k in range(i, i+8):
            for w in range(j, j+8):
                if w % 2 == 0 :
                    if k % 2 == 0 :
                        if arr[k][w] == 'W':
                            b_s += 1
                    else :
                        if arr[k][w] == 'B':
                            b_s += 1
                if w % 2 != 0 :
                    if k % 2 == 0 :
                        if arr[k][w] == 'B':
                            b_s += 1
                    else :
                        if arr[k][w] == 'W':
                            b_s += 1
                if w % 2 == 0 :
                    if k % 2 == 0 :
                        if arr[k][w] == 'B':
                            w_s += 1
                    else :
                        if arr[k][w] == 'W':
                            w_s += 1
                if w % 2 != 0:
                    if k % 2 == 0 :
                        if arr[k][w] == 'W':
                            w_s += 1
                    else :
                        if arr[k][w] == 'B':
                            w_s += 1
        result = min(result, b_s, w_s)
print(result)





