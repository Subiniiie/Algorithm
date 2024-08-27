import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    temp = list(sys.stdin.readline().rstrip())

    arr = []
    for i in range(len(temp)) :
        if i == len(temp)-1 :
            if temp[i] == ')' :
                if len(arr) == 0 or len(arr) > 1 :
                    print('NO')
                else :
                    print('YES')
            else :
                print('NO')
        else :
            if temp[i] == '(' :
                arr.append(temp[i])
            else :
                if len(arr) == 0 :
                    print('NO')
                    break
                else :
                    arr.pop()