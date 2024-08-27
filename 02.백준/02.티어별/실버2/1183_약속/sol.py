import sys
N = int(sys.stdin.readline())
times = []
time_differences = []
for _ in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    times.append([a, b])
    time_differences.append(-(a-b))
time_differences.sort()

min_diffrence = 10**9 - 1
min_diffrence_cnt = 0
for i in range(time_differences[0], time_differences[-1]+1) :
    temp = 0
    for j in range(N) :
        temp += abs(times[j][0] + i - times[j][1])
    if min_diffrence > temp :
        min_diffrence = temp
        min_diffrence_cnt = 1
    elif min_diffrence == temp :
        min_diffrence_cnt += 1
print(min_diffrence_cnt)
