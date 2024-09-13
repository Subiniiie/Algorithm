import sys
N = int(sys.stdin.readline().rstrip())

def fibonacci(N) :
    if N <= 1 :
        return N
    else :
        return fibonacci(N-1) + fibonacci(N-2)


print(fibonacci(N))