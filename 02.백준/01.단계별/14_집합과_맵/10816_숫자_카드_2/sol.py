import sys
N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))


dict = {}
for num in num_lst :
    if num in dict :
        dict[num] += 1
    else :
        dict[num] = 1

for check in check_list :
    if check in dict :
        print(dict[check], end=" ")
    else :
        print(0, end=" ")