arr = [list(input())for _ in range(5)]

max_len = 0
for i in range(5) :
    if max_len < len(arr[i]) :
        max_len = len(arr[i])

for i in range(5) :
    if len(arr[i]) != max_len :
        for j in range(max_len-len(arr[i])) :
            arr[i].append('!')

lst = []
for j in range(max_len) :
    for i in range(5) :
        if arr[i][j] != '!' :
            lst.append(arr[i][j])
print(*lst,sep='')