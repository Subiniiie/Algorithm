import sys
N = int(sys.stdin.readline())

dict = {}
lst = []
for _ in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    if b in dict :
        dict[b].append(a)
    else :
        dict[b] = [a]
        lst.append(b)

lst.sort()

for y in lst :
    if len(dict[y]) == 1 :
        print(dict[y][0], y)
    else :
        dict[y].sort()
        for x in dict[y] :
            print(x, y)