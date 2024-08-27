while True :
    arr = list(map(int, input().split()))
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0 :
        break
    else :
        #가장 긴 변
        m = 0
        #같은 길이
        l = 0
        for i in range(3) :
            if arr[i] > m :
                m = arr[i]
            if i != 2 :
                for j in range(i+1, 3) :
                    if arr[i] == arr[j] :
                        l += 1
        arr.remove(m)
        if m >= sum(arr) :
            print('Invalid')
        else :
            if l == 3 :
                print('Equilateral')
            elif l == 1 :
                print('Isosceles')
            else :
                print('Scalene')


