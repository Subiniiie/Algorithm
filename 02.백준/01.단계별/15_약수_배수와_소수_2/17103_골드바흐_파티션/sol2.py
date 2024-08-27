import sys

arr = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001) :
    if check[i] == 0 :
        arr.append(i)
        for j in range(2*i, 1000001, i) :
            check[j] = 1


T = int(sys.stdin.readline().rstrip())
for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())
    cnt = 0
    for num in arr :
        if num >= N :
            break
        if not check[N-num] and num <= N - num :
            cnt += 1
    print(cnt)