# A : 낮동안 올라가는 높이 B : 밤 동안 떨어지는 높이 V : 나무 높이
A, B, V = map(int, input().split())



if A >= V :
    D = 1

else :
    C = A - B
    if (V - A) % C == 0 :
        D = (V - A) // C + 1
    else :
        D = (V - A) // C + 2

print(D)