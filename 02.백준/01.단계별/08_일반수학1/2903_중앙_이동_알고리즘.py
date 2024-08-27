# 맞았는데 시간 초과

import math

N = int(input())
num_sum = 4

for x in range(N) :
    num = int(math.sqrt(4 ** x))
    print(num)

    for i in range(num) :
        for j in range(num) :
            if i == 0 and j == 0 :
                num_sum += 5
            else :
                if j == 0 :
                    num_sum += 4
                elif i == 0 :
                    num_sum += 4
                else :
                    num_sum += 3

print(num_sum)
