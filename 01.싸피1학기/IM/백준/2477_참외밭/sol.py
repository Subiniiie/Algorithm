K = int(input())
arr = [list(map(int, input().split()))for _ in range(6)]

w = 0
h = 0
w_idx = 0
h_idx = 0

for i in range(6) :
    if arr[i][0] == 1 or arr[i][0] == 2 :
        if w < arr[i][1] :
            w = arr[i][1]
            w_idx = i
    elif arr[i][0] == 3 or arr[i][0] == 4 :
        if h < arr[i][1] :
            h = arr[i][1]
            h_idx = i

garo = abs(arr[(w_idx-1) % 6][1] - arr[(w_idx + 1) % 6][1])
sero = abs(arr[(h_idx-1) % 6][1] - arr[(h_idx + 1) % 6][1])

result = ((w*h) - (garo * sero)) * K
print(result)
