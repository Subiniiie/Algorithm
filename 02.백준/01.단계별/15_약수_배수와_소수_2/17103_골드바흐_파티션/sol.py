import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())
    arr = []
    for i in range(3, N) :
        for j in range(2, int(i**0.5)+1) :
            if i % j == 0 :
                break
        else :
            arr.append(i)

    cnt = 0
    for i in range(len(arr)-1) :
        for j in range(i, len(arr)) :
            if arr[i] + arr[j] == N :
                cnt += 1

    print(cnt)