import sys

max_num = 0
max_num_idx = 0

for i in range(9) :
    n = int(sys.stdin.readline())
    if max_num < n :
        max_num = n
        max_num_idx = i + 1

print(max_num)
print(max_num_idx)