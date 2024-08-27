arr = []
s = 0

for i in range(5) :
    x = int(input())
    s += x
    if i == 0 :
        arr.append(x)
    else :
        if x <= arr[0] :
            arr.insert(0, x)
        elif x >= arr[len(arr) - 1] :
            arr.append(x)
        else :
            for j in range(len(arr) - 1) :
                if arr[j] <= x < arr[j+1] :
                    arr.insert(j+1, x)
                    break
print(s // 5)
print(arr[2])