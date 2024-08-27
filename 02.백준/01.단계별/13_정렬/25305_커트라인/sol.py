# N: 응시자 수, K: 상 받는 사람 수
N, k = map(int, input().split())
# 학생들의 점수
arr = list(map(int, input().split()))

result = []
for i in range(N):
    if i == 0 :
        result.append(arr[i])
    else :
        if arr[i] >= result[0] :
            result.insert(0, arr[i])
        elif arr[i] <= result[-1] :
            result.append(arr[i])
        else :
            for j in range(len(result)):
                if result[j] <= arr[i] < result[j-1]:
                    result.insert(j, arr[i])
                    break
print(result[k-1])