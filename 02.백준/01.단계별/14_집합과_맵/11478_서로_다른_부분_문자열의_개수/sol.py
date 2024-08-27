import sys
S = sys.stdin.readline().rstrip()
result = set()

for i in range(1, len(S)+1) :
    for j in range(len(S)-i+1) :
        if S[j:j+i] not in result :
            result.add(S[j:j+i])
print(len(result))
