import sys
N, M = map(int, sys.stdin.readline().split())
words = []
check_words = []
for _ in range(N) :
    words.append(sys.stdin.readline().rstrip())
for _ in range(M) :
    check_words.append(sys.stdin.readline().rstrip())

set_words = set(words)
cnt = 0
for word in check_words :
    if word in set_words :
        cnt += 1
print(cnt)