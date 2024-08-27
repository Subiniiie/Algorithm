def f(x, y) :
    global seats

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    temp = 1
    i = 0

    while True :
        if temp == K :
            return x + 1, y + 1
        seats[x][y] = 1
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        if 0 <= temp_x < C and 0 <= temp_y < R :
            if seats[temp_x][temp_y] == 0 :
                x = temp_x
                y = temp_y
                temp += 1
            else :
                i = (i + 1) % 4
        else :
            i = (i + 1) % 4


C, R = map(int, input().split())
K = int(input())

seats = [[0 for _ in range(1001)] for _ in range(1001)]

if K > C * R :
    print(0)
else :
    print(*f(0, 0))

