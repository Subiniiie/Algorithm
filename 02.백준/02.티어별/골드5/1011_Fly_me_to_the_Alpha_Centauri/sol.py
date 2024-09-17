import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T) :
    x, y = map(int, sys.stdin.readline().split())

    distance = y - x
    cnt = 0
    move = 1
    move_cnt = 0

    while move_cnt < distance :
        cnt += 1
        move_cnt += move
        if cnt % 2 == 0 :
            move += 1
    print(cnt)
