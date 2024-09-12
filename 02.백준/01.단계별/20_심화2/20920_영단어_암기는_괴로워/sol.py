import sys

N, M = map(int, sys.stdin.readline().split())
dic = {}

for _ in range(N) :
    word = sys.stdin.readline().rstrip()

    if len(word) < M :
        continue
    else :
        if word in dic :
            dic[word] += 1
        else :
            dic[word] = 1

dic = sorted(dic.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in dic :
    print(i[0])

