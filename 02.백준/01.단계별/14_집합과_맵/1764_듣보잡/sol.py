import sys
N, M = map(int, sys.stdin.readline().split())
d = set()
b = set()

for _ in range(N) :
    d.add(sys.stdin.readline().rstrip())

for _ in range(M) :
    b.add(sys.stdin.readline().rstrip())
r = d&b
lst = list(r)
lst.sort()
print(len(lst))
for i in range(len(lst)) :
    print(lst[i])