import sys
N = int(sys.stdin.readline().rstrip())

ride = [[600, 600], [1320, 1320]]
for _ in range(N) :
    a, b = map(str, sys.stdin.readline().split())
    a = int(a[:2]) * 60 + int(a[2:]) - 10
    b = int(b[:2]) * 60 + int(b[2:]) + 10
    ride.append([a, b])

ride.sort()

rest = 0
last = 600

for run, stop in ride :
    rest = max(rest, run - last)
    last = max(last, stop)

print(rest)

