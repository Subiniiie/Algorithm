N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
result = 0


temp = 0
for k in arr :
    if k[1] > result :
        result = k[1]
        idx = temp
    temp += 1

first_h = arr[0][1]

for i in range(idx) :
    if first_h < arr[i+1][1] :
        result += first_h * (arr[i+1][0] - arr[i][0])
        first_h = arr[i+1][1]
    else :
        result += first_h * (arr[i+1][0] - arr[i][0])

first_h = arr[-1][1]

for i in range(N-1, idx, -1) :
    if first_h < arr[i-1][1] :
        result += first_h * (arr[i][0] - arr[i-1][0])
        first_h = arr[i-1][1]
    else :
        result += first_h * (arr[i][0] - arr[i-1][0])
print(result)