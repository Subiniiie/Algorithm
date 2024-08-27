import sys

n = 1
while 1:
    n = int(sys.stdin.readline().rstrip())
    if n == 0 :
        break

    cnt = 0
    for i in range(n + 1, (2 * n) + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else :
            cnt += 1
    print(cnt)