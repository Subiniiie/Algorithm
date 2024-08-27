import sys
N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(M) :
    arr.append(list(map(int, sys.stdin.readline().split())))

if N % 6 == 0 :
    six_set = N // 6
else :
    six_set = N // 6 + 1

price = 100 * 1000
for i in range(M) :
    # 세트로만 사는 경우
    if six_set * arr[i][0] < price :
        price = six_set * arr[i][0]
    # 낱개로만 사는 경우
    if N * arr[i][1] < price :
        price = N * arr[i][1]
    # 세트 + 낱개
    for j in range(M) :
        temp = (N // 6) * arr[i][0] + (N % 6) * arr[j][1]
        if temp < price :
            price = temp
print(price)