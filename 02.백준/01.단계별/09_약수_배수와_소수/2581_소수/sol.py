M = int(input())
N = int(input())

lst = []

for i in range(M, N+1) :
    for j in range(1, i//2+1) :
        if j != 1 and i % j == 0 :
            break
        if j == i//2 :
            lst.append(i)

if len(lst) == 0 :
    print(-1)
else :
    print(sum(lst))
    print(lst[0])