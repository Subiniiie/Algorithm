import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(1, N+1) :
    cnt = 0
    for k in str(i) :
        if k in '369' :
            cnt += 1
    if cnt == 0 :
        print(i, end = ' ')
    else :
        print('-'*cnt, end = ' ')

