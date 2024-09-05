import sys
N = int(sys.stdin.readline().rstrip())
temp = [0]

for i in range(1, N+1) :
    time = sum(list(map(int, sys.stdin.readline().split()))[1:])
    temp.append(time)

temp.sort()
S1 = [0] * (N+1)
S2 = [0] * (N+1)

for j in range(1, N+1) :
    S1[j] = S1[j-1] + temp[j]
    S2[j] = S2[j-1] + S1[j]

print(S2[-1])
