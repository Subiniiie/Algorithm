N = int(input())

for i in range(1, N+1) :
    num = sum(map(int, str(i)))
    sum_num = i + num
    if sum_num == N :
        print(i)
        break
    if i == N :
        print(0)