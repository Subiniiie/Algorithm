import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ondo = list(map(int, input().split()))

result = []
result.append(sum(ondo[:K]))

for i in range(N - K) :
    result.append(result[i] - ondo[i] + ondo[i+K])

print(max(result))