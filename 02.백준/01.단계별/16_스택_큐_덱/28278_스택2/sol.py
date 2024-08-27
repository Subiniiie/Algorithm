import sys

N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N) :
    temp = list(map(int, sys.stdin.readline().split()))
    if len(temp) == 2 and temp[0] == 1 :
        stack.append(temp[1])
    elif len(temp) == 1 :
        if temp[0] == 2 :
            if stack :
                print(stack.pop())
            else :
                print(-1)
        elif temp[0] == 3 :
            print(len(stack))
        elif temp[0] == 4 :
            if stack :
                print(0)
            else :
                print(1)
        elif temp[0] == 5 :
            if stack :
                print(stack[-1])
            else :
                print(-1)
