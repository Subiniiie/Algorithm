N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 도화지는 100x100
# 색종이는 10x10

cnt = 0
result = [[0 for _ in range(101)] for _ in range(101)]
for k in range(N) :
    for i in range(arr[k][0], arr[k][0]+10) :
        for j in range(arr[k][1], arr[k][1]+10) :
            if result[i][j] == 0 :
                result[i][j] = 1
                cnt += 1
print(cnt)


