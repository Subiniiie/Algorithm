import sys
n = int(sys.stdin.readline())

def check(x) :
    for i in range(2, int(x**0.5)+1) :
        if x % i == 0 :
            return False
    return True

for i in range(n) :
    x = int(sys.stdin.readline())
    while True :
        if x == 0 or x == 1 :
            print(2)
            break
        if check(x) :
            print(x)
            break
        else :
            x += 1
