import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    pa = input()
    reversed_pa = pa[::-1]
    if pa == reversed_pa :
        print(f'#{tc}', 1)
    else :
        print(f'#{tc}', 0)