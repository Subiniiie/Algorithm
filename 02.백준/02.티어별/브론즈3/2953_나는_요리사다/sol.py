import sys

max_score = 0
max_cook = 0
for i in range(1, 6) :
    arr = list(map(int, sys.stdin.readline().split()))
    if max_score < sum(arr) :
        max_score = sum(arr)
        max_cook = i
print(max_cook, max_score)