n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_x = -10001
min_x = 10001
max_y = -10001
min_y = 10001

for i in range(n) :
    if arr[i][0] > max_x :
        max_x = arr[i][0]
    if arr[i][0] < min_x :
        min_x = arr[i][0]
    if arr[i][1] > max_y :
        max_y = arr[i][1]
    if arr[i][1] < min_y :
        min_y = arr[i][1]

print((max_x - min_x) * (max_y - min_y))