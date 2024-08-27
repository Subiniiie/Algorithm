import sys
N = int(sys.stdin.readline().rstrip())

i = 3
cnt = 0
while N > i :
    N -= i
    cnt += 1
    i += 2
if N > 0 :
    cnt += 1
print(cnt)