N = int(input())
a = 2 * N

for i in range(a - 1, -1, -2) :
    print(' ' * (i // 2) + '*' * (a - i))
for i in range(3, a, 2) :
    print(' ' * (i // 2) + '*' * (a - i))
