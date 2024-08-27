from collections import deque
import sys
N = int(sys.stdin.readline())
check_words = []
for _ in range(N) :
    check = False
    word = deque(sys.stdin.readline().rstrip())
    for words in check_words :
        if ''.join(list(word)) in words :
            check = True
            break
    if check :
        continue
    words = []
    for _ in range(len(word)) :
        word.rotate(1)
        words.append(''.join(list(word)))
    check_words.append(words)
print(len(check_words))