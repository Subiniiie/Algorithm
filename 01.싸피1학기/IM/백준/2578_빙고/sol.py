chulsoo = [list(map(int, input().split())) for _ in range(5)]
mc = []
for _ in range(5) :
    mc.extend(list(map(int, input().split())))

def f() :
    bingo = 0
    # 가로 확인
    for s in range(5) :
        if chulsoo[s].count(0) == 5 :
            bingo += 1

    # 세로 확인
    for s in range(5) :
        temp = 0
        for w in range(5) :
            if chulsoo[w][s] == 0 :
                temp += 1
        if temp == 5 :
            bingo += 1

    # 왼위 -> 오아 대각선 확인
    temp = 0
    for s in range(5) :
        if chulsoo[s][s] == 0 :
            temp += 1
    if temp == 5 :
        bingo += 1

    # 오위 -> 왼아 대각선 확인
    temp = 0
    for s in range(5) :
        if chulsoo[s][4-s] == 0 :
            temp += 1
    if temp == 5 :
        bingo += 1

    return bingo

cnt = 0
for k in range(25) :
    for i in range(5) :
        for j in range(5) :
            if mc[k] == chulsoo[i][j] :
                chulsoo[i][j] = 0
                cnt += 1

    if cnt >= 12 :
        result = f()

        if result >= 3 :
            print(k+1)
            break