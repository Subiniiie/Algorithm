N = int(input())
arr = list(input() for _ in range(N))

result_cnt = 0
for k in range(N) :
    cnt = 0
    for i in range(len(arr[k])-1) :
        for j in range(i+1, len(arr[k])) :
            if arr[k][j] != arr[k][i + 1] :
                if arr[k][i] != arr[k][i + 1] and arr[k][i] == arr[k][j] :
                    cnt += 1
    if cnt == 0 :
        result_cnt += 1
print(result_cnt)

