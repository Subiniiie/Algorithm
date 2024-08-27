sentence = input()

cnt = 0
for i in sentence :
    if i == ' ' :
        cnt += 1

cnt += 1

for i in range(len(sentence)) :
    if i == 0 :
        if sentence[i] == ' ' :
            if cnt == 2 :
                cnt = 1
            else :
                cnt -= 1
    if i == len(sentence) - 1 :
        if sentence[i] == ' ' :
            if cnt == 2 :
                cnt = 1
            else :
                cnt -= 1
print(cnt)
