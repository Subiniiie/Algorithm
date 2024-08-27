first = int(input())
max_num = 0
max_lst = []

for i in range(1, first+1) :
    arr = [first]
    arr.append(i)

    j = first - i
    while j >= 0 :
        arr.append(j)
        j = arr[-2] - arr[-1]

        if j < 0 :
            break
    if max_num < len(arr) :
        max_num = len(arr)
        max_lst = arr

print(max_num)
print(*max_lst)






