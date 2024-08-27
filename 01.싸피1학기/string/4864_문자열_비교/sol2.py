import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    str1 = input()
    str2 = input()

    check = False

    for i in range(len(str2)) :
        if i + len(str1) <= len(str2) :
            if str1 == str2[i:i+len(str1)] :
                check = True

    if check == True :
        print(f'#{tc}', 1)
    else :
        print(f'#{tc}', 0)
