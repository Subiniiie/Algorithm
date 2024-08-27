import sys

yd = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

arr = []
for _ in range(n) :
    arr.append(sys.stdin.readline().rstrip())

arr.sort()


percent = -1
for name in arr :
    L = yd.count('L') + name.count('L')
    O = yd.count('O') + name.count('O')
    V = yd.count('V') + name.count('V')
    E = yd.count('E') + name.count('E')
    temp = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if percent < temp :
        percent = temp
        result = name
print(result)



