arr = []
for _ in range(3) :
    arr.append(list(map(int, input().split())))


t_x = []
t_y = []
for i in range(3) :
    if arr[i][0] not in t_x :
        t_x.append(arr[i][0])
    else :
        t_x.remove(arr[i][0])
    if arr[i][1] not in t_y :
        t_y.append(arr[i][1])
    else :
        t_y.remove(arr[i][1])
        
print(t_x[0], end=' ')
print(t_y[0])