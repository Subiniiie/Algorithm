import sys
n, m = map(int, sys.stdin.readline().split())

arr = [i for i in range(n+1)]


def union(a, b):
    if (find(a) != find(b)):
        arr[find(b)] = find(a)


def find(a):
    if (arr[a] == a):
        return a
    else:
        arr[a] = find(arr[a])
        return arr[a]


def check(a, b):
    return (find(a) == find(b))

for _ in range(m) :
    x, a, b = map(int, sys.stdin.readline().split())

    if x == 0 :
        union(a, b)
    else :
        if check(a, b) :
            print('YES')
        else :
            print('NO')