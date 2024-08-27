alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z']

dict = {}
k = 9
for key in alpha :
    dict[key] = k + 1
    k += 1

arr = list(input().split())

sum_num = 0
# 10진법을 넘어가는 경우
if int(arr[1]) > 10 :
    for i in range(len(arr[0])) :
        if arr[0][i] in '123456789' :
            sum_num += int(arr[0][i]) * (int(arr[1]) ** (len(arr[0]) - (i+1)))
        else :
            for key in dict.keys() :
                if arr[0][i] == key :
                    sum_num += int(dict[key]) * (int(arr[1]) ** (len(arr[0]) - (i+1)))
# 10진법인 경우
elif int(arr[1]) == 10 :
    sum_num = int(arr[0])

# 10진법을 넘지 않는 경우
else :
    for i in range(len(arr[0])) :
        sum_num += int(arr[0][i]) * (int(arr[1]) ** (len(arr[0]) - (i+1)))


print(sum_num)