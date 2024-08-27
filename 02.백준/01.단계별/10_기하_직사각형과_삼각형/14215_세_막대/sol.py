a, b, c = map(int, input().split())

s = 0
if a == b and a == c :
    print(3 * a)
else :
    if max(a, b, c) == a + b + c - max(a, b, c) :
        print(a + b + c - 1)
    else :
        t = a + b + c - max(a, b, c)
        if t > max(a, b, c) :
            print(a + b + c)
        else :
            print(2 * t  - 1)