import sys

N, M = map(int, sys.stdin.readline().split())
result = []
dict = {}
for _ in range(N) :
    a = sys.stdin.readline().rstrip()

    if len(a) < M :
        continue
    else :
        if a in dict :
            dict[a] += 1
        else :
            dict[a] = 1

num = []
for value in dict.values() :
    if value not in num :
        num.append(value)
num.sort(reverse=True)
for i in num :
    temp = []
    for key, value in dict.items() :
        if i == value :
            temp.append(key)
    temp_dict = {}
    for j in temp :
        if len(j) in temp_dict :
            temp_dict[len(j)].append(j)
        else :
            temp_dict[len(j)] = [j]
    sorted_temp = sorted(temp_dict, reverse=True)
    last_temp = []
    for w in range(len(sorted_temp)) :
        if w != len(sorted_temp) - 1 :
            if len(sorted_temp[w]) != len(sorted_temp[w+1]) :
                print(sorted_temp[w])
            else :
                last_temp.append(sorted_temp[w])




