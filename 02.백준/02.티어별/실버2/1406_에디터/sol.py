import sys
temp = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
arr = []
point = len(temp)
M = len(temp)

result = []


for _ in range(N) :
    arr.append(sys.stdin.readline().strip())

for i in range(N) :
    if arr[i][0] == 'L' :
        if point == 0 :
            continue
        else :
            point -= 1
            result.append(temp.pop())
    elif arr[i][0] == 'D' :
        if point == M :
            continue
        else :
            point += 1
            temp.append(result.pop())
    elif arr[i][0] == 'B' :
        if point == 0 :
            continue
        else :
            temp.pop()
            point -= 1
            M -= 1
    else :
        temp.append(arr[i][2])
        point += 1
        M += 1

for i in temp[::-1] :
    result.append(i)

print(''.join(result[::-1]))