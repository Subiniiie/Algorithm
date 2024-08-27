N = int(input())


# 자기 자신과 각 자리수를 더해서 N이 되는 수를 구해라
result = 0
for i in range(N):
    temp = i
    s = str(i)
    for j in range(len(s)):
        temp += int(s[j])
    if temp == N :
        result = i
        break

print(result)

