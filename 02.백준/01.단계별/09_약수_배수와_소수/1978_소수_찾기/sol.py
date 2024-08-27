N = int(input())
arr = list(map(int, input().split()))

s = N
for i in range(N) :
    if arr[i] == 1:
        s -= 1
    else :
        for j in range(2, arr[i]) :
            if arr[i] % j == 0 :
                s -= 1
                break
print(s)