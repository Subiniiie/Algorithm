import sys

arr = list(sys.stdin.readline().rstrip())

result = 1

if arr[0] == 'c':
    result = 26
else:
    result = 10

for i in range(1, len(arr)):
    if arr[i] == 'c':
        if arr[i - 1] == 'c':
            result *= 25
        else:
            result *= 26
    else:
        if arr[i - 1] == 'c':
            result *= 10
        else:
            result *= 9
print(result)
