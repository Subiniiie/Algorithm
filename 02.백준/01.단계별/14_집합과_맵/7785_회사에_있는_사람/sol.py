import sys
n = int(sys.stdin.readline())
enter_set = set()
for _ in range(n) :
    a, b = sys.stdin.readline().split()
    if b == 'enter' :
        enter_set.add(a)
    else :
        enter_set.remove(a)
lst = list(enter_set)
reversed_name = sorted(lst, reverse=True)
for name in reversed_name :
    print(name)