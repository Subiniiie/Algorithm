arr = [int(input()) for _ in range(3)]

s = 0
l = 0
same = False
for i in range(3):
    s += arr[i]
    if arr[i] == 60:
        l += 1
    if i <= 1 and arr[i] in arr[i+1:3]:
        same = True

if l == 3 :
    print('Equilateral')
else :
    if s == 180:
        if same == True :
            print('Isosceles')
        else :
            print('Scalene')
    else :
        print('Error')