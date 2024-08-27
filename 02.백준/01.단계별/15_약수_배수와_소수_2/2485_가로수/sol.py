import sys
N = int(sys.stdin.readline())

arr = []
sub = []

for i in range(N) :
    arr.append(int(sys.stdin.readline()))
    if i > 0 :
        sub.append(arr[i] - arr[i-1])

# 최대공약수 찾기
# 어케 찾음?

def GCDofTwoNumbers(a, b) :
    while b != 0 :
        a, b = b, a%b
    return a

GCDarr = sub[0]
for i in range(len(sub)) :
    GCDarr = GCDofTwoNumbers(GCDarr, sub[i])

cnt = 0
for num in sub :
    cnt += num // GCDarr - 1
print(cnt)

