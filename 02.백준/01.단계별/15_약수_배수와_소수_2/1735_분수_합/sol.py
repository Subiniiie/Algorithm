import sys
for i in range(2) :
    if i == 0 :
        a, b = map(int, sys.stdin.readline().split())
    else :
        c, d = map(int, sys.stdin.readline().split())

def gcd(a, b) :
    while a % b != 0 :
        mod = a % b
        a = b
        b = mod
    return b

g = gcd(a*d+b*c, b*d)
print((a*d+b*c)//g, (b*d)//g)