import sys
sys.stdin = open('input.txt')

# 슬라이싱으로 회문 판별하는 함수 ---- 1
# for문으로 회문 판별하는 함수 ---- 2
# while문으로 회문 판별하는 함수 ---- 3
# 메서드와 빌트인펑션으로 회문 판별하는 함수 ---- 4


# 1, 2
T = int(input())

for tc in range(1, T+1) :
    str1 = input()
    str2 = input()

    check = 0

    for i in range(len(str2)) :
        if i + len(str1) <= len(str2) :
            if str1 == str2[i:i+len(str1)] :
                check = 1

    if check == 1 :
        print(f'#{tc}', 1)
    else :
        print(f'#{tc}', 0)


# 1, 3
T = int(input())

for tc in range(1, T+1) :
    str1 = input()
    str2 = input()

    i = 0

    check = False
    while i + len(str1) <= len(str2) :
        if str1 == str2[i:i+len(str1)] :
            check = True

        i += 1

    if check == True :
        print(f'#{tc}', 1)
    else :
        print(f'#{tc}', 0)

# 4
T = int(input())

for tc in range(1, T+1) :
    str1 = input()
    str2 = input()

    if str1 in str2 :
        print(f'#{tc}', 1)
    else :
        print(f'#{tc}', 0)
