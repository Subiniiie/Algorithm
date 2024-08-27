import sys
N, M = map(int, sys.stdin.readline().split())
pocketmons = {}
numbers = {}
for i in range(1, N+1) :
    pocketmon = sys.stdin.readline().rstrip()
    pocketmons[str(i)] = pocketmon
    numbers[pocketmon] = str(i)

for _ in range(M) :
    problem = sys.stdin.readline().rstrip()
    if problem in pocketmons :
        print(pocketmons[problem])
    elif problem in numbers :
        print(numbers[problem])

