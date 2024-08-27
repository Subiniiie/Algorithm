# 가로 길이, 세로 길이
garo, sero = map(int, input().split())
number = int(input())
arr = [list(map(int, input().split()))for _ in range(number)]

garo_moeum = []
sero_moeum = []

for k in range(number) :
    if arr[k][0] == 1 :
        garo_moeum.append(arr[k][1])
    else :
        sero_moeum.append(arr[k][1])

garo_moeum.sort()
sero_moeum.sort()

garo_moeum.insert(0, 0)
garo_moeum.append(garo)
sero_moeum.insert(0, 0)
sero_moeum.append(sero)

result = []
for i in range(1, len(garo_moeum)) :
    x = garo_moeum[i] - garo_moeum[i-1]
    for j in range(1, len(sero_moeum)) :
        y = sero_moeum[j] - sero_moeum[j-1]
        result.append(x * y)

result.sort()
print(result[-1])



