N = int(input())
num = 1
cnt = 0
while cnt < N :
    if '666' in str(num) :
        cnt += 1
        if cnt == N :
            print(num)
            break
    num += 1