import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0
check = False
dict = {}
for _ in range(N) :
    temp = sys.stdin.readline().rstrip()
    if check == False and temp == 'ENTER' :
        check = True
    elif check == True and temp != 'ENTER' :
            if temp not in dict :
                dict[temp] = 1
    elif check == True and temp == 'ENTER' :
        for key in dict :
            cnt += 1
        dict = {}
for key in dict:
    cnt += 1
print(cnt)
