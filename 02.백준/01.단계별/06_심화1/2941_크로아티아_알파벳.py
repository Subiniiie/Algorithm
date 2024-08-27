words = input()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
for i in range(len(cro)) :
    if cro[i] in words :
        cnt += words.count(cro[i])

if 'dz=' in words :
    if 'z=' in words :
        cnt -= 1
        temp = len(words) - 3
        if cnt != 1 :
            cnt += temp - ((cnt - 1) * 2)
            print(cnt)
        else :
            cnt += temp
            print(cnt)
    else :
        temp = len(words) - 3
        cnt += temp
        print(cnt)
else :
    cnt += (len(words) - (cnt * 2))
    print(cnt)




