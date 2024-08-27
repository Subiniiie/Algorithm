import sys

N, K = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N+1)]

result = []
idx = 0

for i in range(N) :
    idx += K - 1
    if idx >= len(arr) :
        idx = idx % len(arr)

    result.append(str(arr.pop(idx)))
print("<", ", ".join(result)[:], ">", sep='')