N, M = map(int, input().split())
card = list(map(int, input().split()))

s = 0
for i in range(N) :
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = card[i] + card[j] + card[k]
            if temp > M :
                continue
            else :
                if temp > s :
                    s = temp
print(s)