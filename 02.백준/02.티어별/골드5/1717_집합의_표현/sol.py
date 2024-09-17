import sys
n, m = map(int, sys.stdin.readline().split())

arr = list([i] for i in range(n+1))
for _ in range(m) :
    x, a, b = map(int, sys.stdin.readline().split())
    if x == 0 :
        for i in range(len(arr)) :
            if a in arr[i] :
                temp_list1 = arr[i]
            if b in arr[i] :
                temp_list2 = arr[i]
        arr.append(temp_list1 + temp_list2)
    else :
        for j in range(len(arr)) :
            if a in arr[j] and b in arr[j] :
                print('YES')
                break
            else :
                if j == len(arr) - 1 :
                    print('NO')

