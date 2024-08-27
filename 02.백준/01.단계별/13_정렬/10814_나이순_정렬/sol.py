import sys
N = int(sys.stdin.readline())

dict = {}
lst = []

for _ in range(N) :
    a, b = sys.stdin.readline().split()
    a = int(a)
    if a in dict :
        dict[a].append(b)
    else :
        dict[a] = [b]
        lst.append(a)

lst.sort()

for age in lst :
    if len(dict[age]) == 1 :
        print(age, dict[age][0])
    else :
        for name in dict[age] :
            print(age, name)
