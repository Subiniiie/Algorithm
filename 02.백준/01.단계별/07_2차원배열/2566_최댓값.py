arr = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
for i in range(9) :
    for j in range(9) :
        if max_num <= arr[i][j] :
            max_num = arr[i][j]
            max_x = i
            max_y = j
print(max_num)
print(max_x+1, max_y+1)