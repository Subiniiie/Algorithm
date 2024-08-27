import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))

stack = []
check = 1
for num in arr :
    stack.append(num)
    while stack and stack[-1] == check :
        stack.pop()
        check += 1

if stack :
    print('Sad')
else :
    print('Nice')


