import sys
N = int(sys.stdin.readline().rstrip())

def back(x) :
    if x == 1 or x == 0:
        return 1
    else :
        return x * (back(x-1))


print(back(N))