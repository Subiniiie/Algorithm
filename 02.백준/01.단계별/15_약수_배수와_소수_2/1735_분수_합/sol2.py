import sys

arr = []
for _ in range(2) :
    tempA, tempB = map(int, sys.stdin.readline().split())
    arr.append(tempA)
    arr.append(tempB)
a = arr[0]
b = arr[1]
c = arr[2]
d = arr[3]


# 두 분모의 최소공배수를 찾는다
bb, dd = b, d
b, d = min(b, d), max(b, d)
while b != 0 :
    d = d % b
    b, d = d, b

y = bb * dd // d
x = (y // bb) * a + (y // dd) * c

# 분자와 분모의 최대 공약수를 찾는다
xx, yy = x, y
x, y = min(x, y), max(x, y)
while x != 0 :
    y = y % x
    x, y = y, x
print(xx // y, yy // y)
