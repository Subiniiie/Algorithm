import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N) :
    arr.append(list(map(int, sys.stdin.readline().split())))

result = {}

for i in range(N):
    if arr[i][0] in result :
        result[arr[i][0]].append(arr[i][1])
    else :
        result[arr[i][0]] = [arr[i][1]]

temp = []
for i in result.keys() :
    temp.append(i)
temp.sort()

for i in range(len(temp)) :
    if len(result[temp[i]]) == 1 :
        print(temp[i], result[temp[i]][0])
    elif len(result[temp[i]]) > 1 :
        result[temp[i]].sort()
        for j in range(len(result[temp[i]])) :
            print(temp[i], result[temp[i]][j])