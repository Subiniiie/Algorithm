# / : 나누기, // : 몫, % : 나머지

N = int(input())
cnt = 0

for i in range(N-1, 0, -1):
    if (i * 5) <= N :
        if (N - (i * 5)) % 3 == 0 :
            if (N - ((i - 1) * 5)) % 3 != 0 :
                cnt = i
                N = N - (i * 5)
if N % 3 == 0 :
    cnt += N // 3

if cnt == 0 :
    print(-1)
else :
    print(cnt)