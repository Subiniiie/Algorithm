import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())
arr = deque()

for i in range(1, N+1) :
    arr.append(i)

while len(arr) > 1 :
    arr.popleft()
    a = arr.popleft()
    arr.append(a)
print(arr[0])
