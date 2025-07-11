import sys

# 테스트값 입력받을 때만
# sys.stdin = open("input.txt", "r")
arr = list(map(int, input().split()))

arr.sort()
print(arr[1])