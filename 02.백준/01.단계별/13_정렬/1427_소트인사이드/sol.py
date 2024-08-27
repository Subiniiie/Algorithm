import sys
N = sys.stdin.readline()
arr = []
for i in range(len(N) - 1) :
    arr.append(int(N[i]))
arr.sort(reverse=True)
for j in range(len(arr)) :
    print(arr[j], end="")
