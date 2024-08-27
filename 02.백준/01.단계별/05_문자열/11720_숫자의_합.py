# 첫 번째
N = int(input())
arr = input()

result = []
for i in range(N) :
    result.append(int(arr[i]))
print(sum(result))

# 두 번째
N = int(input())
arr = input()

sum_result = 0
for i in range(N) :
    sum_result += int(arr[i])
print(sum_result)

