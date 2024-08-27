A, B = map(int, input().split())


lst = []
j = B
x = 0
for i in range(1, A+1) :
    if A % i == 0 :
        j -= 1
        lst.append(i)
        if j == 0 :
            if len(lst) == B :
                x = i
            break
print(x)

