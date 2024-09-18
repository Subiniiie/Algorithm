import sys

arr = sys.stdin.readline().rstrip()
result = 0
temp = ''
temp_minus_sum = 0
temp_minus = ''
check = False

for i in arr :
    if check == False :
        if i in '0123456789' :
            temp += i
        elif i == '-' :
            result += int(temp)
            temp = ''
            check = True
        else :
            result += int(temp)
            temp = ''
    else :
        if i in '0123456789' :
            temp_minus += i
        elif i == '+' :
            temp_minus_sum += int(temp_minus)
            temp_minus = ''
        elif i == '-' :
            temp_minus_sum += int(temp_minus)
            temp_minus = ''
if temp_minus :
    temp_minus_sum += int(temp_minus)
result -= temp_minus_sum
if temp :
    result += int(temp)
print(result)

