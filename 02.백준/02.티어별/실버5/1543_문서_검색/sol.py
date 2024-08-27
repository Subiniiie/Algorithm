import sys


sentence = sys.stdin.readline().rstrip()
check = sys.stdin.readline().rstrip()

i = 0
cnt = 0

while i < len(sentence) :
    if sentence[i:i+len(check)] == check :
        i += len(check)
        cnt += 1
    else :
        i += 1
print(cnt)