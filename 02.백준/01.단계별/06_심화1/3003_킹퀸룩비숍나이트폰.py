arr = list(map(int, input().split()))
pieces = [1, 1, 2, 2, 2, 8]

result = []
for i in range(6) :
    result.append(pieces[i] - arr[i])
print(*result)

