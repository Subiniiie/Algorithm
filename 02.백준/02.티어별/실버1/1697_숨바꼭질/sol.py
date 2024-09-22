# 이렇게 푸는 거 아님

import sys
N, K = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(K+1)]

dp[N+1] = 1
for i in range(N+1, K) :
    if i//2 >= N :
        if dp[i+1] != 0 :
            dp[i] = min(dp[i-1], dp[i+1], dp[i//2]) + 1
        else :
            dp[i] = min(dp[i-1], dp[i//2]) + 1
    else :
        if dp[i+1] != 0 :
            dp[i] = min(dp[i-1], dp[i+1]) + 1
        else :
            dp[i] = dp[i-1] + 1

dp[K] = min(dp[K-1], dp[K//2]) + 1

print(dp[K])