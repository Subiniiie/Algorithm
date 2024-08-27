N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
temp_b = []
temp_g = []
for i in range(N) :
    if arr[i][0] == 0 :
        temp_b.append(arr[i][1])
    else :
        temp_g.append(arr[i][1])

for s in range(1, 7) :
    if temp_b.count(s) % K == 0 :
        cnt += temp_b.count(s) // K
    else :
        cnt += temp_b.count(s) // K + 1
    if temp_g.count(s) % K == 0 :
        cnt += temp_g.count(s) // K
    else :
        cnt += temp_g.count(s) // K + 1
print(cnt)



