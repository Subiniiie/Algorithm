import sys
N = int(sys.stdin.readline().rstrip())

arr = []
dict = {}


for _ in range(N) :
    a = int(sys.stdin.readline().rstrip())
    arr.append(a)
    if a in dict :
        dict[a] += 1
    else :
        dict[a] = 1

max_temp = max(dict.values())
max_temp_arr = []

for i in dict :
    if max_temp == dict[i] :
        max_temp_arr.append(i)
max_temp_arr.sort()
if len(max_temp_arr) > 1 :
    temp_idx= max_temp_arr[1]
else :
    temp_idx = max_temp_arr[0]


arr.sort()


print(round(sum(arr) / len(arr)))
print(arr[len(arr)//2])
print(temp_idx)
print(arr[-1] - arr[0])