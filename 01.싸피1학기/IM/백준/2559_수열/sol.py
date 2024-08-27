# 시간 초과

#N : 온도를 측정한 전체 날짜의 수
# K : 합을 구하기 위한 연속적인 날짜의 수

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ondo = list(map(int, input().split()))


for i in range(K - 1, N) :
    if i == K - 1 :
        max_num = sum(ondo[i - K + 1:i + 1])
    else :
        if sum(ondo[i - K + 1:i+ 1]) > max_num :
            max_num = sum(ondo[i - K + 1:i+ 1])

print(max_num)


